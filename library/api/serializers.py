from rest_framework import serializers
from library.models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BooksSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year_of_creating')
