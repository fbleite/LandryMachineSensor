import json
import boto3

print('Loading function')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        image = [key for key in record['dynamodb'] if key.endswith('Image')][0]
        hasStatusChanged = record['dynamodb'][image]['payload']['M']['hasStatusChanged']['BOOL']
        machineStatusOn = record['dynamodb'][image]['payload']['M']['machineStatusOn']['BOOL']
        if (hasStatusChanged):
            arn = 'arn:aws:sns:us-east-1:335553235753:laundryMachineAlert'
            client = boto3.client('sns')
            message = 'Machine turned ' + ('ON' if machineStatusOn else 'OFF')
            client.publish(TargetArn=arn, Message=message)

    return 'Successfully processed {} records.'.format(len(event['Records']))
