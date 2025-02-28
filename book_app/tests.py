from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book

class BookAPITest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Gladys Aloo",
            publication_date="2024-01-01",
            isbn="1234567890123",
            summary="A test book summary."
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.id})

    #get
    def test_get_books_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #get by id
    def test_get_single_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    #create
    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "author": "Gladys Aloo",
            "publication_date": "2023-12-31",
            "isbn": "9876543210123",
            "summary": "Another test book."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    #update
    def test_update_book(self):
        data = {"title": "Updated Book Title"}
        response = self.client.patch(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")
        
    #delete
    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
