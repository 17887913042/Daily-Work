from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Book
import json


class Books(APIView):
    def get(self,request):
        book = Book.objects.get(name='douluodalu')
        # books = Book.objects.all
        data = [{
            "name"   : book.name,
            "author" : book.author,
         }]
        print(data)

        return Response({"error": 0, "message": "success", "data" : data})



