import boto3


class S3Driver:
    UTF_8 = "UTF-8"

    def __init__(self, s3_resource, bucket_name: str):
        self.s3_resource = s3_resource
        self.bucket_name = bucket_name

    @classmethod
    def default(cls, bucket_name: str):
        return cls(boto3.resource("s3"), bucket_name)

    @classmethod
    def create(cls, s3_resource, bucket_name: str):
        return cls(s3_resource, bucket_name)

    def write_to_file(self, content: str, filename: str) -> str:
        to_be_persisted = self.s3_resource.Object(bucket_name=self.bucket_name, key=filename)
        binary_content: bytes = content.encode(self.UTF_8)
        persisted_object: dict = to_be_persisted.put(
            Body=binary_content,
            CacheControl='string',
            ContentDisposition='string',
            ContentEncoding=self.UTF_8,
            ContentLanguage='eng',
            ContentLength=len(binary_content),
        )
        return f's3://{self.bucket_name}/{filename}'
