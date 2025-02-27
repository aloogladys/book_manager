from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer

class BookViewSet(viewsets.ModelViewset):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
