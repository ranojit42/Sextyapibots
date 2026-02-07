from bots_data import bots
import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(bots)
    }