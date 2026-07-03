import boto3
import json
from collections import Counter
from decimal import Decimal

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('cloudwithshad-feedback')


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def lambda_handler(event, context):

    response = table.scan()
    items = response.get("Items", [])

    sentiment_counts = Counter()
    entity_counts = Counter()

    for item in items:
        sentiment = item.get("sentiment", "UNKNOWN")
        sentiment_counts[sentiment] += 1

        entities = item.get("entities", [])
        if isinstance(entities, list):
            for e in entities:
                if isinstance(e, dict):
                    text = e.get("text")
                    if text:
                        entity_counts[text] += 1

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({
            "total_feedback": len(items),
            "sentiment_breakdown": dict(sentiment_counts),
            "top_entities": entity_counts.most_common(10),
            "recent_feedback": items[-10:]
        }, cls=DecimalEncoder)
    }