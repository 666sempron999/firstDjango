from django.shortcuts import render

from django.http import JsonResponse
from .models import Author, Book
from .serializers import AuthorSerializer, BooksSerializer

# Create your views here.

def api_author(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer . data, safe=False)

def api_book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return JsonResponse(serializer . data, safe=False)