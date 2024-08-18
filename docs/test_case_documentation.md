# Non-Automated Test Cases for Google Drive File Downloader

## Test Case 1: Download a File with Removed Access

**Objective**: Ensure that the user is blocked from downloading a file whose access has been manually removed from Google Drive.

- **Preconditions**: 
  - File exists on Google Drive.
  - File access is revoked for the current user (remove sharing permissions).
  
- **Steps**:
  1. Attempt to download the file using the downloader.
  
- **Expected Outcome**:
  - The program should return an appropriate error (e.g., 403 Forbidden) indicating the user has no access.

---

## Test Case 2: Download a File with Transferred Ownership

**Objective**: Verify that the user cannot download a file whose ownership has recently been transferred to another user.

- **Preconditions**: 
  - File exists on Google Drive.
  - Ownership has been transferred from the original owner to another user.
  - New file owner revokes the file access 
  
- **Steps**:
  1. Attempt to download the file using the downloader.
  
- **Expected Outcome**:
  - The program should allow the download.

---

## Test Case 3: Interrupt File Download Using `Ctrl + C`

**Objective**: Observe how the program behaves when a file download is interrupted by a manual `Ctrl + C` operation.

- **Preconditions**: 
  - File download is in progress.
  
- **Steps**:
  1. Start downloading a large file.
  2. Press `Ctrl + C` during the download process.
  
- **Expected Outcome**:
  - The download should be aborted, and the program should exit gracefully without corrupting the partially downloaded file.

---

## Test Case 4: Interrupt File Download by Disabling Internet

**Objective**: Test the program’s behavior when the internet connection is lost during a file download.

- **Preconditions**: 
  - File download is in progress.
  
- **Steps**:
  1. Start downloading a large file.
  2. Disable the internet connection while the download is in progress.
  
- **Expected Outcome**:
  - The program should detect the network failure and terminate the download with an appropriate error message.

---

## Test Case 5: Simultaneous File Downloads

**Objective**: Test the program's behavior when the same file is triggered for download simultaneously.

- **Preconditions**: 
  - File exists on Google Drive.
  
- **Steps**:
  1. Initiate the download of the same file from multiple terminals or processes simultaneously.
  
- **Expected Outcome**:
  - The program should handle the simultaneous download gracefully or prevent duplicate download attempts.

---

## Test Case 6: Multiple Concurrent File Downloads

**Objective**: Observe how the program behaves when multiple file downloads are triggered simultaneously.

- **Preconditions**: 
  - Multiple files exist on Google Drive.
  
- **Steps**:
  1. Trigger downloads for multiple files in parallel.
  
- **Expected Outcome**:
  - The program should handle concurrent downloads without performance degradation or errors.

---

## Test Case 7: Download with Tampered Credentials (Client Email/Secret/token_uri)

**Objective**: Ensure the program throws appropriate errors when the credentials file is tampered with.

- **Preconditions**: 
  - Credentials file (`cred.json`) is altered (client email, secret field, or token URI is modified).
  
- **Steps**:
  1. Attempt to download a file using the tampered credentials file.
  
- **Expected Outcome**:
  - The program should fail with an authentication error.

---

## Test Case 8: Download with Empty Private Key

**Objective**: Ensure the program fails gracefully when the private key in the credentials file is set to `None` or left empty.

- **Preconditions**: 
  - Credentials file (`cred.json`) is modified to have an empty or `None` private key field.
  
- **Steps**:
  1. Attempt to download a file.
  
- **Expected Outcome**:
  - The program should return a clear error indicating that the private key is invalid or missing.

---

## Test Case 9: Download with Empty Client Email

**Objective**: Test the program’s behavior when the client email field is set to `None` or left empty in the credentials file.

- **Preconditions**: 
  - Credentials file (`cred.json`) is modified to have an empty or `None` client email field.
  
- **Steps**:
  1. Attempt to download a file.
  
- **Expected Outcome**:
  - The program should return an error indicating that the client email is invalid or missing.

---

## Test Case 10: Download with Incomplete `cred.json` File

**Objective**: Ensure the program throws a graceful error when key/value pairs are missing from the credentials file.

- **Preconditions**: 
  - `cred.json` is missing key fields (e.g., `client_email`, `private_key`, `token_uri`).
  
- **Steps**:
  1. Attempt to download a file using the incomplete credentials file.
  
- **Expected Outcome**:
  - The program should return a descriptive error message indicating which fields are missing or incomplete.

---

## Test Case 11: Download with Invalid `cred.json` File

**Objective**: Ensure the program throws a graceful error when key/value pairs are invalid in the credentials file.

- **Preconditions**: 
  - `cred.json` contains invalid characters or fields (e.g., `client_email`, `private_key`, `token_uri`).
  
- **Steps**:
  1. Attempt to download a file using the invalid credentials file.
  
- **Expected Outcome**:
  - The program should fail with an authentication or permission-related error.

---

## Test Case 12: Download with Disabled Service Account

**Objective**: Ensure the program fails appropriately when the service account has been disabled in Google Cloud.

- **Preconditions**: 
  - Disable the service account from the Google Cloud Console.
  
- **Steps**:
  1. Attempt to download a file using the disabled service account.
  
- **Expected Outcome**:
  - The program should fail with an authentication or permission-related error.

---

## Test Case 13: Enable Back the Disabled Service Account and Download the File

**Objective**: Ensure the program works appropriately when the service account has been enabled back in Google Cloud.

- **Preconditions**: 
  - Enable the service account back from the Google Cloud Console.
  
- **Steps**:
  1. Attempt to download a file using the enabled service account.
  
- **Expected Outcome**:
  - The program should be able to download the file.

---

## Test Case 14: Download a Large File and Interrupt

**Objective**: Test the program's handling of interruptions during the download of a large file.

- **Preconditions**: 
  - A large file exists on Google Drive.
  
- **Steps**:
  1. Begin downloading the large file.
  2. Interrupt the download midway by closing the terminal or stopping the script.
  
- **Expected Outcome**:
  - The download should be interrupted gracefully, and the partially downloaded file should either be retained or automatically cleaned up.

---

## Test Case 15: Download a File to a Folder with Incorrect Permissions

**Objective**: Ensure the program appropriately handles cases where the destination folder does not have the necessary write permissions.

- **Preconditions**: 
  - A folder exists on the local system where the user does not have write permissions.
  
- **Steps**:
  1. Attempt to download a file and save it to the folder with incorrect permissions.
  
- **Expected Outcome**:
  - The program should return a clear error indicating that the user does not have the necessary permissions to write to the specified folder.

---

## Test Case 16: Download a File to a Drive with Insufficient Disk Space

**Objective**: Test the program's behavior when attempting to download a file to a drive with insufficient disk space.

- **Preconditions**: 
  - The destination drive has less free space available than the size of the file being downloaded.
  
- **Steps**:
  1. Attempt to download a file that is larger than the available space on the destination drive.
  
- **Expected Outcome**:
  - The program should return an appropriate error indicating insufficient disk space, and the download should be aborted without corrupting the partially downloaded file.

---