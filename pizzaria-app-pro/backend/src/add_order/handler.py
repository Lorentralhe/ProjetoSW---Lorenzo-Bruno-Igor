import json
import logging
import os
import uuid
from datetime import datetime
import boto3
from src.common import responses

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs = boto3.client('sqs')
# Esta variável de ambiente foi definida no nosso serverless.yml mais recente
QUEUE_URL = os.environ.get('NEW_ORDERS_QUEUE_URL') 

def handle(event, context):
    try:
        # A lógica de validação continua a mesma
        body = json.loads(event.get('body', '{}'))
        if 'customer' not in body or 'item' not in body:
            return responses.response_400('Campos "customer" e "item" são obrigatórios.')

        # Prepara os dados do pedido para enviar para a fila
        order_data = {
            'orderId': str(uuid.uuid4()),
            'customer': body['customer'],
            'item': body['item'],
            'status': 'PENDING',
            'createdAt': datetime.utcnow().isoformat(),
        }

        # A NOVA LÓGICA: Envia a mensagem para a fila SQS
        sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(order_data)
        )

        logger.info("Pedido %s enfileirado com sucesso.", order_data['orderId'])
        # Responde imediatamente ao cliente com sucesso
        return responses.response_201(order_data)

    except Exception as e:
        logger.error("Erro ao enfileirar pedido: %s", e)
        return responses.response_500()