import json

def lambda_handler(event, context):
    import boto3 #this is what allows us to work with AWS
    import io
    from io import StringIO
    import mimetypes #this does something to the file that allows it to be viewed as a website
    import zipfile # this appears to let me unzip the zip file

    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:315103849162:deployHailsTestTopic')

    try:
        s3 = boto3.resource('s3') #opens s3 for us
        portfolio_bucket = s3.Bucket('jmcconnellportfolio.com') # sets destination folder


        #prints out all of the items in destination folder
        #for obj in portfolio_bucket.objects.all():
        #     print (obj.key)


        build_bucket = s3.Bucket('hailstestbuild.jmcconnellportfolio.com') # set source folder

        #prints out all of the items in the source folder
        #for obj in build_bucket.objects.all():
        #     print (obj.key)

        portfolio_zip = io.BytesIO() # creates an object for the folder to go in

        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip) # puts the zip file into object so it can be unzipped


        # unzips zip file
        with zipfile.ZipFile(portfolio_zip) as myzip:
             for nm in myzip.namelist():
                 # print (nm) #prints files in the zip
                 obj=myzip.open(nm) # unzips file
                 mime_type = mimetypes.guess_type(nm)[0]
                 portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]}) # copies files to destination
                 portfolio_bucket.Object(nm).Acl().put(ACL='public-read') # sets permission

        topic.publish(Subject="HailsTest Deployed", Message="Code for HailsTest Deployed Sucessfully")
    except:
        topic.publish(Subject="HailsTest Deployed", Message="Code for HailsTest Deployed Failed")

    return {
        'statusCode': 200,

    }
