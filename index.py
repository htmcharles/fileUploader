import os
import time
import shutil
import subprocess

# Configuration
MONITOR_FOLDER = "C:/Users/charles/Desktop/MonitorFolder"
UPLOADED_FOLDER = "C:/Users/charles/Desktop/UploadedFolder" 
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"
WAIT_TIME = 30  # (in seconds)

def create_folders():
    """Create the required folders on the desktop if they don't already exist."""
    os.makedirs(MONITOR_FOLDER, exist_ok=True)
    os.makedirs(UPLOADED_FOLDER, exist_ok=True)

def monitor_and_upload():
    """Monitors a folder, uploads images, and moves them after successful upload."""
    while True:
        try:
            files = [f for f in os.listdir(MONITOR_FOLDER) if os.path.isfile(os.path.join(MONITOR_FOLDER, f))]

            for file_name in files:
                file_path = os.path.join(MONITOR_FOLDER, file_name)

                time.sleep(WAIT_TIME)

                try:
                    response = subprocess.run([
                        "curl", "-X", "POST", "-F", f"imageFile=@{file_path}", UPLOAD_URL
                    ], capture_output=True, text=True)

                    # Check if the upload was successful
                    if response.returncode == 0:
                        print(f"Uploaded: {file_name}")

                        # Move the file to the uploaded folder
                        uploaded_path = os.path.join(UPLOADED_FOLDER, file_name)
                        shutil.move(file_path, uploaded_path)
                        print(f"Moved {file_name} to {UPLOADED_FOLDER}")
                    else:
                        print(f"Failed to upload {file_name}: {response.stderr}")

                except Exception as e:
                    print(f"Error uploading {file_name}: {e}")

        except Exception as e:
            print(f"Error monitoring folder: {e}")

        time.sleep(5)

if __name__ == "__main__":
    create_folders()
    print("Starting folder monitoring...")
    monitor_and_upload()
