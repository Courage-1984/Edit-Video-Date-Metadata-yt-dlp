import subprocess
import sys
from datetime import datetime

def modify_metadata(file_path, upload_date, download_date):

    # Check if upload_date is "NA" (not available)
    if upload_date == "NA":
        print("Upload date not available. Skipping metadata modification.")
        return

    # Convert the upload date to the desired format
    upload_date_formatted = datetime.strptime(upload_date, "%Y%m%d").strftime("%Y:%m:%d %H:%M:%S")
    
    # Get the current date and time in the desired format
    current_date_formatted = datetime.utcnow().strftime("%Y:%m:%d %H:%M:%S%z")

    # Provide the full path to exiftool.exe
    exiftool_path = r'C:\Users\diete\Desktop\cli_rippers\yt\exiftool.exe'

    # Modify metadata using exiftool
    subprocess.run([exiftool_path,
                   '-overwrite_original',  # Add this line to prevent backup file creation
                   '-ReleaseDate=' + upload_date_formatted,
                   '-FileModifyDate=' + upload_date_formatted,
                   '-CreateDate=' + current_date_formatted,
                   file_path])

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 4:
        print("Usage: script.py <file_path> <upload_date> <download_date>")
        sys.exit(1)

    # Use sys.argv[1] directly without additional modifications
    file_path = sys.argv[1]
    upload_date = sys.argv[2].strip("'")  # Remove single quotes around upload_date
    download_date = sys.argv[3].strip("'")  # Remove single quotes around download_date

    modify_metadata(file_path, upload_date, download_date)
