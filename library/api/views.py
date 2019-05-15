
from library.models import Book
from .serializers import BooksSerializer
from rest_framework import generics

class PurchaseList(generics.ListAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Book.objects.filter(purchaser=user)


