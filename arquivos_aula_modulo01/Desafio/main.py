from datetime import datetime

records = [
    {
        'source': '48-996355555',
        'destination': '48-666666666',
        'end': 1564610974,
        'start': 1564610674
    },
    {
        'source': '41-885633788',
        'destination': '41-886383097',
        'end': 1564506121,
        'start': 1564504821
    },
    {
        'source': '48-996383697',
        'destination': '41-886383097',
        'end': 1564630198,
        'start': 1564629838
    },
    {
        'source': '48-999999999',
        'destination': '41-885633788',
        'end': 1564697158,
        'start': 1564696258
    },
    {
        'source': '41-833333333',
        'destination': '41-885633788',
        'end': 1564707276,
        'start': 1564704317
    },
    {
        'source': '41-886383097',
        'destination': '48-996384099',
        'end': 1564505621,
        'start': 1564504821
    },
    {
        'source': '48-999999999',
        'destination': '48-996383697',
        'end': 1564505721,
        'start': 1564504821
    },
    {
        'source': '41-885633788',
        'destination': '48-996384099',
        'end': 1564505721,
        'start': 1564504821
    },
    {
        'source': '48-996355555',
        'destination': '48-996383697',
        'end': 1564505821,
        'start': 1564504821
    },
    {
        'source': '48-999999999',
        'destination': '41-886383097',
        'end': 1564610750,
        'start': 1564610150
    },
    {
        'source': '48-996383697',
        'destination': '41-885633788',
        'end': 1564505021,
        'start': 1564504821
    },
    {
        'source': '48-996383697',
        'destination': '41-885633788',
        'end': 1564627800,
        'start': 1564626000
    }
]


# Calcula a tarifa de uma chamada
def calculate_call_bill(start, end):

    # Registra a hora inicial e final da ligação
    time_start = datetime.fromtimestamp(start)
    time_end = datetime.fromtimestamp(end)

    # Se a ligação está no período noturno retorna o valor base
    if (time_start.hour >= 22 or time_end.hour < 6):
        return 0.36

    # Se o fim da ligação estiver fora do período de cobrança
    # Cobra o tempo até às 22 horas
    elif (time_end.hour >= 22):
        time_end = datetime(time_end.year, time_end.month,
                            time_end.day, 22)

    # Se o começo da ligação estiver fora do período de cobrança
    # Cobra o tempo começando às 06 horas
    elif (time_start.hour < 6):
        time_start = datetime(time_start.year, time_start.month,
                              time_start.day, 6)

    # Calcula o tempo de ligação, converte para segundos
    # e faz uma floor division (divisão que arredonda o valor para o piso)
    call_time = (time_end - time_start).seconds // 60

    # Retorna a cobrança pelo tempo de ligação mais a tarifa base
    return 0.36 + call_time * 0.09


def classify_by_phone_number(records):

    # Cria um conjunto com o número dos clientes
    # Conjuntos (set) mantém elementos únicos sem repetição
    sources = set(record['source'] for record in records)

    # Cria as contas a serem pagas para cada cliente no final
    bills = [{'source': bill, 'total': 0.00} for bill in sources]

    # For para iterar por cada registro de ligação
    for record in records:

        # Registrar qual cliente é a origem da ligação
        source = record['source']

        # Calcula o custo da ligação
        call_bill = calculate_call_bill(record['start'], record['end'])

        # Salva o custo da ligação na conta total do cliente
        # E arredonda os valores na segunda casa decimal
        for bill in bills:
            if bill['source'] == source:
                bill['total'] += call_bill
                bill['total'] = round(bill['total'], 2)

    # Ordena os valores das contas de forma decrescente
    bills.sort(key=lambda k: k['total'], reverse=True)

    return bills
