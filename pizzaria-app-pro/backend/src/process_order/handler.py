import json
import logging
from src.common import database

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    try:
        # O evento da SQS pode conter múltiplos registros (pedidos)
        for record in event['Records']:
            order_data = json.loads(record['body'])
            order_id = order_data.get('orderId')

            logger.info("Processando pedido da fila: %s", order_id)
            
            # Chama a função no nosso módulo de banco de dados para salvar o item
            database.create_order_from_item(order_data)
            
            logger.info("Pedido %s salvo no DynamoDB com sucesso.", order_id)

    except Exception as e:
        logger.error("Falha ao processar pedido da fila: %s", e)
        # Lançar o erro faz com que a SQS tente reenviar a mensagem mais tarde
        raise e