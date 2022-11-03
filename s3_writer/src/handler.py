import os
from s3_driver import S3Driver
from datetime import datetime
import uuid


def handle_request(event, context) -> str:
    now = datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")
    content = f'hello s3 from lambda {now_string}'
    s3_driver = S3Driver.default(bucket_name())
    s3_driver.write_to_file(content, str(uuid.uuid4()))
    return "OK"


def bucket_name():
    return str(os.environ.get("S3_BUCKET"))
