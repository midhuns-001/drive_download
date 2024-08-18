import argparse
import sys
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def authenticate_drive(credentials_file):
    """
    Authenticate and create the Google Drive service.

    :param credentials_file: Path to the credentials JSON file.
    :return: Authenticated Google Drive service instance.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=['https://www.googleapis.com/auth/drive']
        )
        service = build('drive', 'v3', credentials=credentials)
        logger.info("Authentication successful.")
        return service
    except FileNotFoundError:
        logger.error(f"Credentials file not found: {credentials_file}")
        sys.exit(-1)
    except Exception as e:
        logger.error(f"Failed to authenticate Google Drive: {e}")
        sys.exit(-1)

def list_files(service):
    """
    List the files and file IDs that are shared with the authenticated service account.

    :param service: Authenticated Google Drive service instance.
    """
    try:
        results = service.files().list(pageSize=100, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(f"{item['name']} ({item['id']})")
    except HttpError as error:
        logger.error(f"An HTTP error occurred: {error}")
    except Exception as e:
        logger.error(f"An error occurred while listing files: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verify & get files that are shared with the service account')

    parser.add_argument('--credentials', required=True, type=str, help='Path to the Google Drive API credentials JSON file')

    args = parser.parse_args()

    # Check if the credentials argument is provided
    if not args.credentials:
        logger.error("The credentials file path is required. Use --credentials to specify the path.")
        sys.exit(-1)

    try:
        service = authenticate_drive(args.credentials)
        list_files(service)
    except Exception as e:
        logger.error(f"Failed to list files: {e}")
        sys.exit(-1)
