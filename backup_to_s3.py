import os
import zipfile
import boto3
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
REGION_NAME = os.getenv('AWS_REGION', 'us-east-1')

def zip_directory(folder_path, zip_path):
    """Compresses a target directory into a zip file."""
    print(f"Archiving folder: {folder_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Successfully created archive: {zip_path}")

def upload_to_s3(file_name, bucket, object_name=None):
    """Uploads a file to an AWS S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Initialize the S3 client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION_NAME
    )

    try:
        print(f"Uploading {file_name} to S3 bucket '{bucket}'...")
        s3_client.upload_file(file_name, bucket, object_name)
        print("Upload successful!")
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return False
    return True

def main():
    # Configuration
    target_folder = './data_to_backup'  # Folder to back up
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"backup_{timestamp}.zip"

    # Ensure there's a dummy folder to backup if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        with open(os.path.join(target_folder, 'dummy_data.txt'), 'w') as f:
            f.write("This is important data that needs to be backed up to the cloud.")

    # Execute workflow
    zip_directory(target_folder, zip_filename)
    
    # Only attempt upload if S3 bucket is configured
    if BUCKET_NAME and BUCKET_NAME != "your_s3_bucket_name_here":
        upload_to_s3(zip_filename, BUCKET_NAME)
    else:
        print("Skipping AWS upload: AWS_S3_BUCKET_NAME not configured in .env")

    # Clean up local zip file
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
        print("Cleaned up local temporary zip file.")

if __name__ == "__main__":
    main()
