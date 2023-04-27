# Automation of creation and renewal of Let's Encrypt free TLS certificates using Certbot, python and Terraform


The certcreator folder contains python script using Certbot python library, creating a single TLS certificate and then uploading it to an S3 bucket of your choice.

The lambda-renew-certs folder contains example of AWS lambda fucntion python that crawls through all TLS certificates found in S3 bucket named "certificates-bucket" in an attempts to renew them if their expiry date is < 30 days. 
