from library.models import Author, Book
from .serializers import AuthorSerializer, BooksSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Book site api')


class AuthorViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_fields = ('title', 'description')


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BooksSerializer



