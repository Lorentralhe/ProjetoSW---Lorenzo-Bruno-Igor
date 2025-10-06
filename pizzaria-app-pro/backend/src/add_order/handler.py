import json
import logging
from src.common import responses, database

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        if 'customer' not in body or 'item' not in body:
            return responses.response_400('Campos "customer" e "item" são obrigatórios.')

        new_order = database.create_order(body)
        logger.info("Pedido criado: %s", new_order['orderId'])
        return responses.response_201(new_order)

    except Exception as e:
        logger.error("Erro ao criar pedido: %s", e)
        return responses.response_500()