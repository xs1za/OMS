from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from store.models import Book
from store.serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

