from rest_framework import serializers
from bookapi.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','nome','descricao','nota']
        