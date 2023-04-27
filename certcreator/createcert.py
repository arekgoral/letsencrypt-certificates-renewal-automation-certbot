# Creates let's encrypt TLS certificate using DNS challenge and uploads the certificates to an S3 bucket.

import boto3
import certbot.main
import os

def create_certificate(domain_name, bucket_name, key_name):
    # Create an S3 client
    s3 = boto3.client('s3')

     # Create a temp directory if it doesn't exist
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Create a new certificate using Certbot
    certbot.main.main([
        '-v',
        'certonly',
        '--preferred-challenges', 'dns',
        '--manual',
        '--work-dir','temp',
        '--config-dir', 'temp',
        '--logs-dir', 'temp',
        '-d', domain_name])

    # Upload the certificate files to S3
    with open(temp_dir + '/live/' + domain_name + '/privkey.pem', 'rb') as f:
        s3.upload_fileobj(f, bucket_name, key_name + '/privkey.pem')
    with open(temp_dir + '/live/' + domain_name + '/fullchain.pem', 'rb') as f:
        s3.upload_fileobj(f, bucket_name, key_name + '/fullchain.pem')

# Example usage (adjust domain name, name of the S3 bucket and name of key in the S3 bucket)
create_certificate('testdomain.net', 'certificates_bucket', 'mycerts')