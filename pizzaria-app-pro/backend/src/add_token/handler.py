import json
import logging
from src.common import responses, database

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        if 'deviceToken' not in body:
            return responses.response_400('Campo "deviceToken" é obrigatório.')

        database.create_token(body)
        logger.info("Token adicionado com sucesso.")
        return responses.response_201({'message': 'Token adicionado com sucesso.'})

    except Exception as e:
        logger.error("Erro ao adicionar token: %s", e)
        return responses.response_500()