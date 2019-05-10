from rest_framework import serializers
from library.models import Author, Book



class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BooksSerializer(serializers.HyperlinkedModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year_of_creating')
