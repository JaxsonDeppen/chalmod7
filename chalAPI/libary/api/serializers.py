from rest_framework import serializers
from libary.models import Author, Book, Loan


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author']

class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()  

    class Meta:
        model = Loan
        fields = ['id', 'book', 'borrower', 'loan_date', 'return_date']
