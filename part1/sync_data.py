import os
import requests
import boto3

S3_BUCKET = "rearc-quest-bucket-abhijaya-2025"

DATA_FILES = [
    ("pr.data.1.AllData", "https://download.bls.gov/pub/time.series/pr/pr.data.1.AllData"),
    ("pr.series", "https://download.bls.gov/pub/time.series/pr/pr.series"),
]

s3 = boto3.resource("s3")
bucket = s3.Bucket(S3_BUCKET)

print("Fetching existing files from S3 bucket...")
existing_files = [obj.key for obj in bucket.objects.all()]
print(f"Found {len(existing_files)} existing files in S3.")

for file_name, url in DATA_FILES:
    if file_name in existing_files:
        print(f"Skipping {file_name}, already exists in S3.")
        continue

    print(f"Downloading {url}...")

    # Adding browser User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Uploading {file_name} to S3...")
        bucket.put_object(Key=file_name, Body=response.content)
        print(f"Uploaded {file_name} successfully!")
    else:
        print(f"Failed to download {file_name}: HTTP {response.status_code}")
