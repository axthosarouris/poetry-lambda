import os
import uuid

from faker import Faker

from s3_driver import S3Driver


def handle_request(event, context) -> str:
    content = Faker().name()

    s3_driver = S3Driver.default(bucket_name())
    s3_driver.write_to_file(content, str(uuid.uuid4()))
    return "OK"


def bucket_name():
    return str(os.environ.get("S3_BUCKET"))
