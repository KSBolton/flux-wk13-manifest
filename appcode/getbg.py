import os
import boto3

BGIMAGE = os.environ.get("BGIMAGE") 

s3 = boto3.client("s3")
split_str = BGIMAGE.split('/')
try:
    s3.download_file(Bucket=split_str[2],
                    Key=split_str[-1], Filename="/app/static/img/bgimg.jpg")
except NoCredentialsError as e:
    print(e)                    