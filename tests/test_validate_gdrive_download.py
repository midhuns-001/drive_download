"""
    Tests to download file from Google Drive and validate
"""
import os, logging
import pytest
import json
from utils.file_utility import run_program, validate_results

# Load test data from the JSON file
with open(os.path.join('test_data', 'test_data.json'), 'r') as f:
    test_data = json.load(f)
    if os.path.exists(test_data['VALID_DESTINATION']):
        os.remove(test_data['VALID_DESTINATION'])

logger = logging.getLogger()

@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['VALID_FILE_IDS']]
)
def test_download_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a file - file id: {file_id}, file permission: {comment}")
    result = run_program([file_id, test_data["VALID_DESTINATION"], '--credentials', cred_file])
    validate_results(file_id, test_data["VALID_DESTINATION"], result)


def test_download_file_shared_by_another_user(cred_file):
    logger.info(f"Download a file shared by another user")
    result = run_program([test_data['SHARED_FILE_ID'], test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(test_data['SHARED_FILE_ID'], test_data['VALID_DESTINATION'], result)

@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['DOC_FILE_TYPES']]
)
def test_download_doc_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a DOC file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['SPREADSHEET_FILE_TYPES']]
)
def test_download_spreadsheet_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a SPREADSHEET file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['PPT_FILE_TYPES']]
)
def test_download_ppt_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a PPT file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['IMAGE_FILE_TYPES']]
)
def test_download_image_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a IMAGE file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['AUDIO_FILE_TYPES']]
)
def test_download_audio_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a AUDIO file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['VIDEO_FILE_TYPES']]
)
def test_download_video_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a VIDEO file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['ARCHIVE_FILE_TYPES']]
)
def test_download_archive_file_types_valid_file_id(file_id, comment, cred_file):
    logger.info(f"Download a ARCHIVE file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['SCRIPTS_FILE_TYPES']]
)
def test_download_scripts_file_types_valid_file_id(file_id, comment):
    print(f"Download a SCRIPT/CODE file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', 'json_cred.json'])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['APPLICATION_FILE_TYPES']]
)
def test_download_application_file_types_valid_file_id(file_id, comment):
    print(f"Download an APPLICATION file - file id: {file_id}, file type: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', 'json_cred.json'])
    validate_results(file_id, test_data['VALID_DESTINATION'], result)


def test_download_folder_id_invalid(cred_file):
    folder_id = test_data['FOLDER_ID']
    logger.info(f"Download a folder with folder id: {folder_id}")
    result = run_program([test_data['FOLDER_ID'], test_data['VALID_DESTINATION'], '--credentials', cred_file])
    assert result.returncode != 0
    assert "Unsupported Google Docs Editors file type: application/vnd.google-apps.folder" in result.stdout


@pytest.mark.parametrize(
    "file_id, comment",
    [(item['file_id'], item['comment']) for item in test_data['INVALID_FILE_IDS']]
)
def test_download_invalid_file_ids(file_id, comment, cred_file):
    logger.info(f"Download a file with an file ID: {file_id}, Comment: {comment}")
    result = run_program([file_id, test_data['VALID_DESTINATION'], '--credentials', cred_file])
    assert "file_cache is only supported with oauth2client" in result.stdout


def test_download_valid_file_id_insufficient_permissions(cred_file):
    logger.info(f"Download a file with insufficient privileges")
    result = run_program([test_data['INSUFFICIENT_PERMISSIONS_FILE_ID'], test_data['VALID_DESTINATION'], '--credentials', cred_file])
    assert result.returncode != 0
    assert "file_cache is only supported with oauth2client" in result.stdout


def test_invalid_destination(cred_file):
    logger.info(f"Download a file to a non-existing destination folder")
    result = run_program([test_data['VALID_FILE_ID'], test_data['INVALID_DESTINATION'], '--credentials', cred_file])
    assert result.returncode != 0
    assert "file_cache is only supported with oauth2client" in result.stdout


@pytest.mark.skip(reason="not implemented")
def test_download_file_whose_access_is_removed():
    """
    1. Download a file whose access is manually removed
    2. User should be blocked from downloading the file
    """
    pass


@pytest.mark.skip(reason="not implemented")
def test_download_file_whose_ownership_is_transferred():
    """
    1. Download a file whose ownership is recently transferred
    2. User should be blocked from downloading the file
    """
    pass


#@pytest.mark.skip(reason="Takes time to execute")
def test_download_large_file_test_2gb(cred_file):
    """
    1. Download a file whose size is 2G or above
    2. User should be able to download the file successfully
    3. Verify the file size / checksum
    """
    logger.info(f"Download a file whose size is 2G or above")
    result = run_program([test_data['LARGE_FILE_ID'], test_data['VALID_DESTINATION'], '--credentials', cred_file])
    validate_results(test_data['LARGE_FILE_ID'], test_data['VALID_DESTINATION'], result)


@pytest.mark.skip(reason="not implemented")
def test_interrupt_file_download():
    """
    1. Download a file and interrupt the program in the middle
    2. Use Ctrl +C or disable internet while download is in progress
    2. Verify the behavior
    """
    pass


@pytest.mark.skip(reason="not implemented")
def file_download_concurrently():
    """
    1. Trigger same file download concurrently and observe the behavior
    2. Verify the behavior
    """
    pass


@pytest.mark.skip(reason="not implemented")
def file_download_multiple_files_concurrently():
    """
    1. Trigger multiple file download concurrently and observe the behavior
    2. Verify the behavior
    """
    pass

