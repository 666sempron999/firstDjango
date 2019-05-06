from rest_framework import serializers
from .models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BooksSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('author', 'title', 'description', 'year_of_creating')

        # fields = (Author.objects.filter(repo_id__pk=1), 'title', 'description', 'year_of_creating')

