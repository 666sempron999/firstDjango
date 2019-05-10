from library.api.viewsets import AuthorViewSet, BookViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)