import boto3
import os

s3 = boto3.client('s3')
bucket = os.getenv("S3_BUCKET", "ecommerce-data")

s3.upload_file('snowflake/sample_data.csv', bucket, 'raw/sales.csv')
print('Uploaded to S3.')