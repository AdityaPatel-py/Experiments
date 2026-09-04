import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def resize_image(bucket, key, output_bucket):
    print(f"Downloading {key} from {bucket}...")
    obj = s3.get_object(Bucket=bucket, Key=key)
    img = Image.open(io.BytesIO(obj['Body'].read()))

    print("Resizing...")
    img = img.resize((200, 200))

    buffer = io.BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)

    output_key = f"resized-{key}"
    print(f"Uploading {output_key} to {output_bucket}...")
    s3.put_object(Bucket=output_bucket, Key=output_key, Body=buffer, ContentType="image/jpeg")
    print("✅ Done!")

if __name__ == "__main__":
    resize_image("image-resizer-bucket-0-to-9", "images.jpg", "image-resizer-bucket-0-to-9")

