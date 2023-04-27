import boto3
from certbot import main as certbot_main

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('certificates_bucket')
    for obj in bucket.objects.filter(Prefix='mycerts/'):
        if obj.key.endswith('.pem'):
            certbot_main(['renew', '--cert-name', obj.key[:-4], '--force-renewal'])