# AWS S3 Automated Backup Script

A Python-based cloud computing utility designed to automate the process of archiving local directories and securely uploading them to Amazon S3. 

This project demonstrates programmatic interaction with AWS Cloud Services, file I/O operations, and environment variable management for secure credentials handling.

## Features
* **Automated Compression:** Uses Python's native `zipfile` library to recursively compress target directories.
* **AWS Integration:** Utilizes `boto3` (The AWS SDK for Python) to authenticate and upload objects to an S3 bucket.
* **Secure Credentials:** Implements `python-dotenv` to ensure AWS Access Keys and Secret Keys remain outside the source code, adhering to cloud security best practices.
* **Auto-Cleanup:** Automatically deletes the local `.zip` file after a successful cloud upload to save local disk space.

## Tech Stack
* **Python 3.x**
* **AWS S3** (Cloud Storage)
* **Boto3** (AWS SDK)
* **Dotenv** (Environment Management)

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/NikhilBhima-24/aws-s3-auto-backup.git](https://github.com/NikhilBhima-24/aws-s3-auto-backup.git)
   cd aws-s3-auto-backup
Install dependencies:

Bash
pip install -r requirements.txt
Configure AWS Credentials:

Copy the example environment file: cp .env.example .env

Open .env and enter your actual AWS Access Key, Secret Key, and S3 Bucket name.

Usage
Run the script directly from the terminal. By default, it will look for a folder named data_to_backup, compress it, append a timestamp to the filename, and upload it to your configured S3 bucket.

Bash
python backup_to_s3.py
