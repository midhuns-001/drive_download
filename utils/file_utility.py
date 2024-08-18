
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import subprocess

# Authenticate and create the Google Drive service
def authenticate_drive():
    # Path to your service account key file
    credentials_file = os.path.join('config', 'cred.json')

    # Authenticate using the service account file
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=['https://www.googleapis.com/auth/drive']
    )

    # Build the Drive service
    service = build('drive', 'v3', credentials=credentials)
    return service


# Function to get the file size from file ID
def get_file_size_from_gdrive(file_id):
    service = authenticate_drive()

    # Get file metadata
    file_metadata = service.files().get(fileId=file_id, fields="name, size").execute()

    # Extract file size
    file_name = file_metadata.get('name')
    file_size = file_metadata.get('size')

    if file_size:
        print(f"File Name: {file_name}")
        print(f"File Size: {int(file_size)} bytes")
    else:
        print(f"File {file_name} has no size (may be a Google Drive native file).")
    return int(file_size)

def get_file_size(file_path):
    with open(file_path, 'rb') as f:
        file_size = os.fstat(f.fileno()).st_size
    return file_size

# Helper function to run the download program with given arguments
def run_program(args):
    command = ['python3', os.path.join('src', 'download_files_gdrive.py')] + args
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

def validate_results(file_id, destination, result):
    assert "File downloaded successfully" in result.stdout
    assert result.returncode == 0

    file_size_gdrive = get_file_size_from_gdrive(file_id)
    file_size_downloaded = get_file_size(destination)
    assert file_size_gdrive == file_size_downloaded, "Mismatch in gdrive file size vs downloaded file size"

    if os.path.exists(destination):
        os.remove(destination)