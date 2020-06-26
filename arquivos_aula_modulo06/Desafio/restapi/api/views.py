from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter


@api_view(['POST'])
def question(request):
    # Pega os dados que estão no campo question da requisição
    data = request.data['question']

    # Faz a contagem dos números e ordena das mais recorrentes
    # para as menos.
    number_counter = Counter(data).most_common()

    # Cria o vetor final de para resposta
    result = []

    for number in number_counter:
        # Pega o número e cria um vetor com aquele número repetido
        # number[1] vezes. Após isso adiciona os elementos desse
        # vetor intermediário no vetor final.
        result.extend([number[0]]*number[1])

    return Response({"solution": result})