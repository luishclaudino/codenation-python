import requests


# Classe customizada para tipificar o erro.
# Se eu passar uma string como parâmetro, ela pode
# ser usada como uma msg de erro customizada.
class RequestError(Exception):
    pass


# Função para converter para Celsius
def convert_to_celsius(temperature):
    return int((temperature - 32) * 5.0 / 9.0)


def get_temperature(lat, lng, key):
    # Retirei a key da função tanto por questão de segurança
    # Como para fazer testes de key inválida
    url = f'https://api.darksky.net/forecast/{key}/{lat},{lng}'
    response = requests.get(url)
    data = response.json()

    # Se houve um erro na url de requisição, devolve a mensagem de erro
    if data.get('error'):
        raise RequestError(data.get('error') + ' Check your url request.')

    # if not temperature nunca ocorria por conta do AttributeError
    # Então coloquei essa verificação para ficar mais compreensível.
    # Pois o campo currently é um campo opcional de acordo com a doc da API.
    if not data.get('currently').get('temperature'):
        raise RequestError('Data not found. Check your url request.')

    temperature = data.get('currently').get('temperature')

    temperature_in_celsius = convert_to_celsius(temperature)

    return temperature_in_celsius
