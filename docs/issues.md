# Known Issues in Google Drive File Downloader

## Issue 1: Corrupt or Stale File Creation When Interrupted by `Ctrl + C`

**Description**: 
- When the download process is interrupted by pressing `Ctrl + C` or the program is killed during execution, a corrupt or stale file is created.

**Impact**:
- The partially downloaded file may be unusable and could take up disk space unnecessarily.

**Suggested Fix**:
- Implement a mechanism to clean up partially downloaded files when the program is interrupted, or handle the interruption gracefully to ensure file integrity.

---

## Issue 2: Network Interruption Fails to Resume Download

**Description**: 
- If the download is interrupted due to a network issue, the program fails to resume and complete its execution after the network is restored. A retry mechanism is not implemented.

**Impact**:
- Users need to restart the download process manually, which can be inefficient, especially for large files.

**Suggested Fix**:
- Implement a retry mechanism to automatically resume the download process when the network connection is re-established.

---

## Issue 3: File Overwriting in Simultaneous Downloads from Multiple Terminals

**Description**: 
- When the same file is being downloaded simultaneously from different terminals, the program overwrites the file, leading to potential data loss or corruption.

**Impact**:
- The integrity of the downloaded file is compromised, and simultaneous downloads cannot be safely performed.

**Suggested Fix**:
- Implement file locking or error handling logic to prevent simultaneous writes to the same destination file.

---

## Issue 4: Security Risk with Private Key Validation

**Description**: 
- There is a serious security risk as the program does not strictly validate the private key. Modifying or appending certain symbols (e.g., `!`, `$`, `==`) to the private key still allows the authentication to go through.

**Impact**:
- This poses a significant security vulnerability, as unauthorized access could be gained with an improperly validated key.

**Suggested Fix**:
- Implement strict validation of the private key to ensure its integrity and authenticity before proceeding with any operations.
    