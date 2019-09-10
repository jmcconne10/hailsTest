import boto3
from botocore.client import Config
import StringIO
import zipfile

s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('jmcconnellportfolio.com')
build_bucket - s3.Bucket('hailstestbuild.jmcconnellportfolio.com')

portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('jmcconnellportfolio.com', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_zip.Object(nm).Acl().put(ACL='public-read')
