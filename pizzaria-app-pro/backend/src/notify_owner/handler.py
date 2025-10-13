import json
import logging
import os
import boto3
from boto3.dynamodb.types import TypeDeserializer

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')
TOPIC_ARN = os.environ.get('ORDER_EVENTS_TOPIC_ARN')

def unmarshall(dynamodb_item):
    """Converte um item no formato DynamoDB JSON para um dicionário Python normal."""
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in dynamodb_item.items()}

def handle(event, context):
    try:
        for record in event['Records']:
            # Só processa eventos de inserção de novos pedidos
            if record['eventName'] == 'INSERT':
                new_image = record['dynamodb']['NewImage']
                
                # Converte o formato do DynamoDB para um JSON simples
                order_data = unmarshall(new_image)
                order_id = order_data.get('orderId', 'ID_DESCONHECIDO')
                item_name = order_data.get('item', 'Item desconhecido')

                # Prepara a mensagem a ser publicada
                subject = f"Novo Pedido Recebido: #{order_id[:8]}"
                message_body = (
                    f"Um novo pedido foi criado!\n\n"
                    f"ID do Pedido: {order_id}\n"
                    f"Cliente: {order_data.get('customer')}\n"
                    f"Item: {item_name}\n"
                    f"Status: {order_data.get('status')}"
                )

                # Publica a mensagem no tópico SNS
                sns.publish(
                    TopicArn=TOPIC_ARN,
                    Subject=subject,
                    Message=message_body
                )
                logger.info("Evento de novo pedido (%s) publicado no SNS.", order_id)

    except Exception as e:
        logger.error("Erro ao publicar evento no SNS: %s", e)
        raise e