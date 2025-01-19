# Python Script to Monitor and Upload Images

## Objective
This Python script is designed to automate the following tasks:

1. **Monitor a folder** where a camera regularly saves captured pictures.
2. **Automatically upload each picture** after 30 seconds using the `curl` command.
3. Once a picture is successfully uploaded, **move it to another folder** named `uploaded` to avoid redundancy.

## Requirements

- **Python**: Version 3.6 or later
- **Curl**: Installed and accessible via the command line
- **Operating System**: Compatible with Windows

### Upload URL
The script uploads images to the following URL:
```
https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php
```

The attribute `imageFile` is used to specify the image file during upload.

### Example curl Command
```
curl -X POST -F imageFile=@/path/to/your/image.jpg <upload_url>
```

## How It Works

1. **Create Folders**: The script ensures that the folders for monitoring (`MonitorFolder`) and uploaded images (`UploadedFolder`) exist.
2. **Monitor Folder**: It continuously checks the `MonitorFolder` for new files.
3. **Upload Files**: Each new file is uploaded using the `curl` command after a 30-second delay.
4. **Move Files**: Upon successful upload, the file is moved to the `UploadedFolder` to avoid redundant uploads.

## Configuration
The following variables can be modified as needed:

- **`MONITOR_FOLDER`**: Path to the folder being monitored. Default:
  ```
  C:/Users/charles/Desktop/MonitorFolder
  ```

- **`UPLOADED_FOLDER`**: Path to the folder where uploaded files are moved. Default:
  ```
  C:/Users/charles/Desktop/UploadedFolder
  ```

- **`UPLOAD_URL`**: URL where the images are uploaded. Default:
  ```
  https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php
  ```

- **`WAIT_TIME`**: Time in seconds to wait before uploading a file. Default: `30` seconds.

## Setup Instructions

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Install Curl**: Ensure that `curl` is installed and accessible via the command line. On Windows, this can be verified by typing `curl --version` in the Command Prompt.
3. **Download Script**: Save the provided Python script as `image_uploader.py`.
4. **Run Script**: Open a terminal or Command Prompt and run the script:
   ```
   python image_uploader.py
   ```
5. **Place Files**: Save any images you want to upload in the `MonitorFolder`.

## Output

- Successfully uploaded images will be moved to the `UploadedFolder`.
- Any errors during the upload process will be logged in the terminal.

## Example Output
```plaintext
Starting folder monitoring...
Uploaded: image1.jpg
Moved image1.jpg to C:/Users/charles/Desktop/UploadedFolder
Uploaded: image2.jpg
Moved image2.jpg to C:/Users/charles/Desktop/UploadedFolder
```

## Notes

- Ensure the `MonitorFolder` path is accessible and writable.
- The `curl` command must have sufficient permissions to execute and upload files.
- Network connectivity is required for successful uploads.

## License
This script is open-source and free to use for personal and commercial purposes.

