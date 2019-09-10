import boto3
import io
from io import StringIO
import mimetypes

s3 = boto3.resource('s3')
portfolio_bucket = s3.Bucket('jmcconnellportfolio.com')
for obj in portfolio_bucket.objects.all():
     print (obj.key)

#portfolio_bucket.download_file('index.html', '/tmp/index.html')
build_bucket = s3.Bucket('hailstestbuild.jmcconnellportfolio.com')
for obj in build_bucket.objects.all():
     print (obj.key)

#build_bucket.download_file('portfoliobuild.zip', '/tmp/portfoliobuild.zip')


portfolio_zip = io.BytesIO()

build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

import zipfile
with zipfile.ZipFile(portfolio_zip) as myzip:
     for nm in myzip.namelist():
         print (nm)
         obj=myzip.open(nm)
         mime_type = mimetypes.guess_type(nm)[0]
         portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
         portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
