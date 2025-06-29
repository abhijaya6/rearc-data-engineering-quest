import boto3
import pandas as pd
from io import BytesIO

bucket_name = "rearc-quest-bucket-abhijaya-2025"
s3 = boto3.client("s3")

# Files you want to process
files = ["pr.data.1.AllData", "pr.series"]

for file_name in files:
    print(f"Downloading {file_name} from S3...")
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = obj["Body"].read()
    
    # Convert file bytes to pandas DataFrame assuming tab-separated values
    df = pd.read_csv(BytesIO(file_content), sep="\t")
    
    print(f"{file_name} DataFrame shape: {df.shape}")
    print(df.head())  # Show first few rows to confirm parsing
