import dateutil.parser
from datetime import datetime, timedelta

import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

print('Loading function')
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('LaundryMachineState')


def lambda_handler(event, context):
    currentDateString = event['queryStringParameters']['timestamp']
    endDate = dateutil.parser.parse(currentDateString)

    window = int(event['queryStringParameters']['window'])
    startDate = endDate - timedelta(minutes=window)

    response = table.query(
        KeyConditionExpression=Key('deviceId').eq(1) & Key('timestamp').between(startDate.isoformat(),
                                                                                endDate.isoformat()),
        ScanIndexForward=False
    )

    points = []

    for item in response['Items']:
        point = {
            'machineStatusOn': item['machineStatusOn'],
            'timestamp': item['timestamp'],
            'currentIntensity': float(item['currentIntensity']),
            'deviceId': int(item['deviceId'])
        }
        points.append(point)

    body = {
        'points': points
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body),
        "isBase64Encoded": False,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }
    return response