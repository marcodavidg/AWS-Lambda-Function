import json

def lambda_handler(event, context):
    name = str(event['queryStringParameters']['name'])
    response = f'Hello there {name}. From AWS Lamba!'
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
