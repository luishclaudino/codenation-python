from main import get_temperature, RequestError, convert_to_celsius
import requests
import pytest


# Classe customizada para realizar o mock
# Ela vai sobrescrever requests.Response
# retornado pelo requests.get
class MockResponse:
    def __init__(self, resposta):
        self.resposta = resposta

    # Substitui o método json() para retornar o que eu definir
    # como resposta na criação
    def json(self):
        return self.resposta


# As fixtures abaixo são funções executadas antes de cada teste
# em que são aplicadas. Normalmente fixtures são usadas
# para fornercer dados para os testes
@pytest.fixture
def latitude():
    return -14.235004


@pytest.fixture
def longitude():
    return -51.92528


@pytest.fixture
def key():
    return 'e1ee55658d4a2b28c4841e373c3b3d87'


def test_get_temperature_by_lat_lng(monkeypatch, latitude, longitude, key):

    reposta_mock = {"currently": {"temperature": 62}}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # Retorna o valor convertido em celsius
    result = get_temperature(latitude, longitude, key)
    assert result == 16


# Os mocks com erros dos testes abaixo foram feitos de acordo com
# as mensagens de erro retornados pela API.
# Mas esses erros podem ser feitos por verificações simples, retornando
# mensagens feitas pelo programador.


# Testando uma key de acesso inválida
def test_wrong_key(monkeypatch, latitude, longitude):
    key = 'e1ff55658d4a2b28c4841e373c3b3d87'

    reposta_mock = {"error": "permission denied"}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # É esperado que com esses parâmetros seja retornado
    # um erro do tipo RequestError
    with pytest.raises(RequestError):
        get_temperature(latitude, longitude, key)


# Testando sem um parâmetro necessário no request
def test_without_one_request_parameter(monkeypatch, latitude, longitude, key):
    # Como na função esse valor se torna string
    # Então atribui uma string vazia para testar a omissão.
    no_parameter = ''

    reposta_mock = {"error": "Poorly formatted request"}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # Teste sem latitude
    with pytest.raises(RequestError):
        get_temperature(no_parameter, longitude, key)

    # Teste sem longitude
    with pytest.raises(RequestError):
        get_temperature(latitude, no_parameter, key)

    # Teste sem key
    with pytest.raises(RequestError):
        get_temperature(latitude, longitude, no_parameter)


# Teste da conversão para graus celsius
def test_convert_to_celsius_function():

    temperature_fahrenheit = 62

    assert convert_to_celsius(temperature_fahrenheit) == 16


def test_invalid_latitude(monkeypatch, longitude):

    reposta_mock = {"error": "The given location is invalid."}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # Valore de latitudes são válidas no range entre -90 e 90
    with pytest.raises(RequestError):
        latitude = 91.05418
        get_temperature(latitude, longitude, key)

    with pytest.raises(RequestError):
        latitude = -91.05418
        get_temperature(latitude, longitude, key)


def test_invalid_longitude(monkeypatch, latitude):

    reposta_mock = {"error": "The given location is invalid."}

    # Função que substitui o get retornando um objeto
    # com a resposta que eu defini
    def mock_get(*args, **kwargs):
        return MockResponse(reposta_mock)
    # Aplica o mock na função get do requests
    monkeypatch.setattr(requests, "get", mock_get)

    # Valores de longitude são válidas no range entre -180 e 180
    with pytest.raises(RequestError):
        longitude = -181.052
        get_temperature(latitude, longitude, key)

    with pytest.raises(RequestError):
        longitude = 181.052
        get_temperature(latitude, longitude, key)
