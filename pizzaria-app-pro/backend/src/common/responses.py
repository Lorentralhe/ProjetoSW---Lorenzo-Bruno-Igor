import json

def _build_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }

def response_200(data): return _build_response(200, data)
def response_201(data): return _build_response(201, data)
def response_400(message): return _build_response(400, {'message': message})
def response_404(message="Recurso não encontrado."): return _build_response(404, {'message': message})
def response_500(message="Erro interno do servidor."): return _build_response(500, {'message': message})