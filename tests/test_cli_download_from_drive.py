import pytest, json, os, logging

from conftest import cred_file
from utils.file_utility import run_program

logger = logging.getLogger()

@pytest.fixture(autouse=True)
def cleanup_directories():
    with open('test_data/test_data.json', 'r') as f:
        data = json.load(f)
    if os.path.exists(data['VALID_DESTINATION']):
        os.remove(data['VALID_DESTINATION'])
    yield


def test_missing_arguments():
    logger.info(f"Test that the script fails when required arguments are missing.")
    result = run_program([])
    assert result.returncode != 0
    assert "error: the following arguments are required: file_id, destination" in result.stderr


def test_missing_file_id():
    logger.info(f"Test that the script fails when file_id is missing.")
    result = run_program(["destination.txt"])
    assert result.returncode != 0
    assert f"error: the following arguments are required: destination" in result.stderr


def test_missing_destination(test_data_dict):
    logger.info(f"Test that the script fails when destination is missing.")
    result = run_program([test_data_dict['VALID_FILE_ID']])
    assert result.returncode != 0
    assert f"error: the following arguments are required: destination" in result.stderr


def test_invalid_file_id(cred_file, test_data_dict):
    logger.info(f"Test the script with an invalid file ID.")
    result = run_program(["invalid_file_id", test_data_dict['VALID_DESTINATION'], '--credentials', cred_file])
    assert result.returncode != 0
    assert "file_cache is only supported with oauth2client" in result.stdout


def test_valid_download(cred_file, test_data_dict):
    logger.info(f"Test the script with valid file IDs.")
    result = run_program([test_data_dict['VALID_FILE_ID'], test_data_dict['VALID_DESTINATION'], "--credentials", cred_file])
    assert result.returncode == 0
    assert "File downloaded successfully to" in result.stdout


def test_invalid_credentials(invalid_cred_file, test_data_dict):
    logger.info(f"Test the script with invalid credentials by giving a wrong  private key.")
    result = run_program([test_data_dict['VALID_FILE_ID'], test_data_dict['VALID_DESTINATION'], "--credentials", invalid_cred_file])
    assert result.returncode != 0, "ERROR: Command returned success. "
    assert "Failed to authenticate Google Drive" in result.stdout


@pytest.mark.skip(reason="not implemented")
def test_missing_credentials():
    logger.info(f"Test the download script with missing credentials.")
    """
    1. Create a json file where credentials are missing or empty
    2. Make private_key null 
    3. Or make client_email as null
    4. Validate both the conditions
    5. User should not be able to download the file successfully in either cases.
    """
    pass

@pytest.mark.skip(reason="not implemented")
def test_insufficient_credentials():
    """
    1. Use insufficient credentials to download a file
    2. use private key
    2. User should not be able to download the file successfully
    """
    pass


@pytest.mark.skip(reason="not implemented")
def test_download_file_by_disable_service_account():
    logger.info(f"Test the Download script by disabling service account.")
    """
    1. Go to Google console and disable the service account
    4. Validate the download file operation
    5. User should not be able to download the file successfully in either cases.
    """
    pass


@pytest.mark.skip(reason="not implemented")
def test_download_file_by_disable_network():
    logger.info(f"Test the Download script by disabling network")
    """
    1. Trigger the download script
    2. While the script is running, disable internet
    3. Validate the download file operation
    4. User should not be able to download the file successfully
    """
    pass

@pytest.mark.skip(reason="not implemented")
def test_partial_download_by_interruption():
    logger.info(f"Test the Download script by interrupting the download ")
    """
    1. Trigger the download script
    2. While the script is running, please Ctrl + C or kill the process
    3. Validate the download file operation. Check the stack trace
    4. Check the file is stale and its actual size.
    5. User should not be able to download the file successfully.
    """
    pass