import os
import boto3
from uuid import uuid4
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
orders_table = dynamodb.Table(os.environ.get('ORDERS_TABLE_NAME'))
tokens_table = dynamodb.Table(os.environ.get('TOKENS_TABLE_NAME'))

def create_order(order_data):
    timestamp = datetime.utcnow().isoformat()
    item = {
        'orderId': str(uuid4()),
        'customer': order_data['customer'],
        'item': order_data['item'],
        'status': 'PENDING',
        'createdAt': timestamp,
    }
    orders_table.put_item(Item=item)
    return item

def update_order_status(order_id, new_status):
    result = orders_table.update_item(
        Key={'orderId': order_id},
        UpdateExpression="set #status = :s",
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={':s': new_status},
        ReturnValues="UPDATED_NEW"
    )
    return result.get('Attributes')

def create_token(token_data):
    item = {
        'tokenId': str(uuid4()),
        'deviceToken': token_data['deviceToken'],
    }
    tokens_table.put_item(Item=item)
    return item

def get_all_tokens():
    response = tokens_table.scan(ProjectionExpression="deviceToken")
    return [item['deviceToken'] for item in response.get('Items', [])]