import logging
from src.common import database

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    try:
        tokens = database.get_all_tokens()
        if not tokens:
            logger.warning("Nenhum token encontrado para notificar.")
            return

        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                new_image = record['dynamodb']['NewImage']
                order_id_short = new_image['orderId']['S'][:8]
                item_name = new_image['item']['S']
                message = f"Nova pizza no forno! Pedido #{order_id_short} de {item_name}."

                for token in tokens:
                    logger.info("NOTIFICANDO token %s: %s", token, message)

    except Exception as e:
        logger.error("Erro ao processar stream do DynamoDB: %s", e)
        raise e