import boto3
import json


client = boto3.client('lambda')
event = {
    "path": "/",
    "headers": {
        "Content-Type": "application/json"
    },
    "resource": "/",
    "httpMethod": "GET",
    "queryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "body": ""
}

response = client.invoke(
    FunctionName='cha-lambda-dev-handler',
    InvocationType='RequestResponse',
    Payload=bytes(json.dumps(event), 'utf-8'),
    Qualifier='$LATEST'
)
res = json.loads(response['Payload'].read().decode("utf-8"))
print(res)
