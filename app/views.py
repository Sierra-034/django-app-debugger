from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MyView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'operation success'})
