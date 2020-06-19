from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter


@api_view(['POST'])
def question(request):
    data = request.data['question']
    number_counter = Counter(data).most_common()
    result = []
    for number in number_counter:
        result.extend([number[0]]*number[1])

    return Response({"solution": result})