import boto3
import json
import uuid
from datetime import datetime

comprehend = boto3.client('comprehend')
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('cloudwithshad-feedback')

CORS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
}

def lambda_handler(event, context):
    print("EVENT:", json.dumps(event))

    try:
        method = event.get('requestContext', {}).get('http', {}).get('method')

        if method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': CORS,
                'body': ''
            }

        body = json.loads(event.get('body', '{}'))

        name = body.get('name', '')
        email = body.get('email', '')
        message = body.get('message', '')[:5000]

        sentiment = comprehend.detect_sentiment(
            Text=message,
            LanguageCode='en'
        )

        entities_raw = comprehend.detect_entities(
            Text=message,
            LanguageCode='en'
        )

        entities = [
            {
                'text': e['Text'],
                'type': e['Type']
            }
            for e in entities_raw.get('Entities', [])[:10]
        ]

        feedback_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'feedback_id': feedback_id,
                'name': name,
                'email': email,
                'message': message,
                'sentiment': sentiment['Sentiment'],
                'entities': entities,
                'submitted_at': datetime.utcnow().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'headers': CORS,
            'body': json.dumps({
                'success': True,
                'id': feedback_id,
                'sentiment': sentiment['Sentiment']
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            'statusCode': 500,
            'headers': CORS,
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }