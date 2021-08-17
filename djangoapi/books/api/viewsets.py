from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksVieweSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerealizer
    queryset = models.Books.objects.all()
