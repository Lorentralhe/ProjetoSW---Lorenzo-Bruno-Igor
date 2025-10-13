import os
import boto3
from uuid import uuid4
from datetime import datetime

# MODIFICADO: A inicialização das tabelas foi removida daqui
dynamodb = boto3.resource('dynamodb')

# --- Funções para a tabela de Pedidos ---

def create_order_from_item(order_item):
    """Salva um item de pedido completo vindo da fila SQS no DynamoDB."""
    # MOVIDO PARA DENTRO DA FUNÇÃO: A tabela só é inicializada quando a função é chamada
    orders_table = dynamodb.Table(os.environ.get('ORDERS_TABLE_NAME'))
    orders_table.put_item(Item=order_item)
    return order_item

def update_order_status(order_id, new_status):
    """Atualiza o status de um pedido."""
    orders_table = dynamodb.Table(os.environ.get('ORDERS_TABLE_NAME'))
    result = orders_table.update_item(
        Key={'orderId': order_id},
        UpdateExpression="set #status = :s",
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={':s': new_status},
        ReturnValues="UPDATED_NEW"
    )
    return result.get('Attributes')

# --- Funções para a tabela de Tokens ---

def create_token(token_data):
    """Salva um novo token de notificação."""
    tokens_table = dynamodb.Table(os.environ.get('TOKENS_TABLE_NAME'))
    item = {
        'tokenId': str(uuid4()),
        'deviceToken': token_data['deviceToken'],
    }
    tokens_table.put_item(Item=item)
    return item

def get_all_tokens():
    """Busca todos os tokens de notificação."""
    tokens_table = dynamodb.Table(os.environ.get('TOKENS_TABLE_NAME'))
    response = tokens_table.scan(ProjectionExpression="deviceToken")
    return [item['deviceToken'] for item in response.get('Items', [])]