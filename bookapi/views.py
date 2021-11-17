from rest_framework import viewsets
import bookapi
from bookapi import serializer
from bookapi.models import Book
from bookapi.serializer import BookSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

