import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('testTable')

    response = table.query(
        KeyConditionExpression=Key('name').eq('Danny')
    )

  #  for i in response['Items']:
    #    print(i['RideDayTime'], ":", i['rideDate'])


    data = []

    for i in response['Items']:
        item = {"RideDayTime": i['rideDateTime'}
        for attribute in attributes_selected:
            if attribute.feature == feature:
                item[attribute.attribute.name] = attribute.value
        data.append(item)

    jsonData=json.dumps(data)

    return {
        'statusCode': 200,
        #'rideDayTime': rideDayTime
    }

    #return(submitter, rideDate)
