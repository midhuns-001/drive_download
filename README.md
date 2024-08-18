
# Download Files from Google Drive and Test the Application

## Overview

This repository provides a solution for downloading files from Google Drive using Python and also includes a test automation framework to validate the functionality.

### Contents

1. **src**: Source code for downloading files from Google Drive.
2. **verify files util**: Utility to get file IDs from shared files.
3. **Test Automation Framework**: Framework for automating tests for the file downloader.
4. **Test Case Documentation**: Detailed document outlining non-automated test cases.

## Folder Structure

```plaintext
.
├── src/
│   └── download_from_gdrive.py  # Main Python script for downloading files
├── tests/
│   └── test_cli_download_from_drive.py       # Test scripts using `pytest`
|   └── test_validate_gdrive_download.py      # Test scripts using `pytest`
├── docs/
│   └── test_case_documentation.md      # Documentation of test cases
│   └── issues.md                       # Documentation of issues
├── config/
│   └── cred.json                       # Sample valid credentials JSON file
│   └── invalid_cred.json               # Sample invalid credentials JSON file
├── test_data/
│   └── test_data.json                  # Sample input test data
├── utils/
│   └── file_utility.py                 # Utility files used by the test code
```

## Tech Stack

- **Python**: Core programming language.
- **Pytest**: Testing framework for writing and running tests.

## Prerequisites

### 1. Setup Google Drive API Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Google Drive API for your project.
3. Create a service account and download the credentials JSON file.
4. Place the credentials file (e.g., `cred.json` and `invalid_cred.json`) in the `config/` directory.
5. Place the test data in file `test_data/test_data.json`

### 2. Install Required Python Packages

#### Install `pipenv`

To manage dependencies and virtual environments, install `pipenv`:

```bash
pip3 install pipenv
# Or if you're on a Mac, you can use Homebrew:
brew install pipenv
```

#### Install Project Dependencies

Navigate to your project directory and install the dependencies listed in the `Pipfile`:

```bash
pipenv install
pipenv shell
```

## How to Run the Code

1. Ensure your credentials JSON file (`cred.json`) is correctly configured in the `config/` directory.
2. Execute the download script using the following command:

   ```bash
   python3 src/download_from_gdrive.py <file_id> <destination> --credentials config/cred.json
   ```

   - Replace `<file_id>` with the Google Drive file ID.
   - Replace `<destination>` with the local path where the file should be saved.

## How to Run the Tests

1. Ensure your `cred.json` is set up in the `config/` directory.
2. Prepare the test data in the `test_data/` directory as required.
3. Run the tests using `pytest`:

   ```bash
   pytest --html=report.html
   ```

   This command will generate an HTML report (`report.html`) summarizing the test results.

## Test Reporting

The test results are detailed in an HTML report (`report.html`). This report includes pass/fail statuses, logs, and error messages for each test case.

## Test Case Documentation

Test case documentation is available in the `docs/` directory and includes:

1. **Test Scenarios**: Detailed scenarios covering positive and negative cases (documented in the `tests/` folder).
2. **Uncovered Scenarios**: Scenarios that could not be automated in time.
3. **Future Enhancements**: Suggestions for additional test cases and potential improvements.

## Issues Found

Any issues discovered during testing or execution are documented in the `docs/issues.md` file. This includes:

- Description of the issue.
- Steps to reproduce.
