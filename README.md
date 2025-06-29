Rearc Data Engineering Quest
This project completes the Rearc Data Engineering Quest as described in the README requirements:

Part 1 & 2
Fetched BLS Productivity and Costs data (pr.data.1.AllData.txt and pr.series.txt) from the given endpoint.

Uploaded the data to my S3 bucket: [s3://rearc-quest-bucket-abhijaya-2025/](https://eu-north-1.console.aws.amazon.com/s3/buckets/rearc-quest-bucket-abhijaya-2025?region=eu-north-1&bucketType=general&tab=objects).

Converted and uploaded the population.json file to the same bucket.

Part 3
Wrote and executed Python scripts to:

Load pr.data.1.AllData.txt and population.json from S3.

Merge productivity data with population data for the years 2013–2018.

Calculate and print the required statistics.

Outputs were verified in logs and notebooks.

Part 4
As discussed, I did not implement the infrastructure automation (CDK/Terraform) due to time constraints.

Usage
Scripts for parts 1–3 are available in the part1, part2, and part3 folders.

Credentials and bucket permissions are configured for public read access to JSON/CSV files.
