
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
print('Loading function')
dynamo = boto3.resource('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''

    table = dynamo.Table('LaundryMachineState')
    
    response = table.query(
        KeyConditionExpression=Key('deviceId').eq(1), 
        Limit=1,
        ScanIndexForward = False,
        
    )

    # body = '{{"machineStatusOn": {status}, "timestamp": {timestamp}}}'.format(
    #     status=response['Items'][0]['machineStatusOn'],
    #     timestamp = response['Items'][0]['timestamp']
    #     )
        
    body = {
            'machineStatusOn': response['Items'][0]['machineStatusOn'],
            'timestamp': response['Items'][0]['timestamp']
            }
        

    return {
        'statusCode': '200',
        'body': body,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

