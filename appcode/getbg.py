import os
import boto3
from botocore.exceptions import NoCredentialsError

BGIMAGE = open("/etc/webappinfo/bgimage")

s3 = boto3.client("s3")

try:
    split_str = BGIMAGE.split('/')
except (AttributeError) as e:
    print(e)

try:
    s3.download_file(Bucket=split_str[2],
                    Key=split_str[-1], Filename="/app/static/img/bgimg.jpg")
except (NoCredentialsError) as e:
    print(e)                    