import logging
from src.common import responses, database

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    try:
        order_id = event['pathParameters']['orderId']
        updated_order = database.update_order_status(order_id, 'RECEIVED')

        if not updated_order:
            return responses.response_404("Pedido não encontrado.")

        logger.info("Status do pedido %s atualizado para RECEIVED", order_id)
        return responses.response_200(updated_order)

    except Exception as e:
        logger.error("Erro ao atualizar pedido %s: %s", event.get('pathParameters', {}).get('orderId'), e)
        return responses.response_500()