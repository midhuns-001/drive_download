import os
import io
import sys
import logging
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError

# Configure logging to redirect stdout and stderr
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class GoogleDriveDownloader:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.service = self.authenticate_drive()

    def authenticate_drive(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file, scopes=['https://www.googleapis.com/auth/drive']
            )
            service = build('drive', 'v3', credentials=credentials)
            logger.info("Authentication successful.")
            return service
        except Exception as e:
            logger.error(f"Failed to authenticate Google Drive: {e}")
            sys.exit(-1)

    def get_file_metadata(self, file_id):
        try:
            file = self.service.files().get(fileId=file_id, fields='mimeType').execute()
            return file['mimeType']
        except HttpError as error:
            logger.error(f"An HTTP error occurred while retrieving metadata: {error}")
            raise
        except Exception as e:
            logger.error(f"An error occurred while retrieving metadata: {e}")
            raise

    def download_file(self, file_id, destination):
        mime_type = self.get_file_metadata(file_id)

        try:
            if mime_type.startswith('application/vnd.google-apps'):
                # Handle Google Docs Editors files
                export_mime_types = {
                    'application/vnd.google-apps.document': 'application/pdf',
                    'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
                }
                export_mime_type = export_mime_types.get(mime_type)
                if not export_mime_type:
                    logger.error(f"Unsupported Google Docs Editors file type: {mime_type}")
                    sys.exit(-1)

                request = self.service.files().export_media(fileId=file_id, mimeType=export_mime_type)
                with io.FileIO(destination, 'wb') as fh:
                    downloader = MediaIoBaseDownload(fh, request)
                    done = False
                    while not done:
                        status, done = downloader.next_chunk()
                        logger.info(f"Export and download {int(status.progress() * 100)}%.")
            else:
                # Handle binary files
                request = self.service.files().get_media(fileId=file_id)
                with io.FileIO(destination, 'wb') as fh:
                    downloader = MediaIoBaseDownload(fh, request)
                    done = False
                    while not done:
                        status, done = downloader.next_chunk()
                        logger.info(f"Download {int(status.progress() * 100)}%.")
            logger.info(f"File downloaded successfully to {destination}.")
        except HttpError as error:
            if error.resp.status == 404:
                logger.error(f"Error: File not found with ID {file_id}.")
                return error.resp
            else:
                logger.error(f"An HTTP error occurred: {error}")
            raise
        except Exception as e:
            logger.error(f"An error occurred during the download: {e}")
            raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from Google Drive')
    parser.add_argument('file_id', type=str, help='The ID of the file on Google Drive')
    parser.add_argument('destination', type=str, help='The local path where the file should be saved')
    parser.add_argument('--credentials', type=str,
                        help='Path to the Google Drive API credentials JSON file')

    args = parser.parse_args()

    try:
        downloader = GoogleDriveDownloader(credentials_file=args.credentials)
        downloader.download_file(args.file_id, args.destination)
    except Exception as e:
        logger.error(f"Failed to download file: {e}")
        sys.exit(1)
