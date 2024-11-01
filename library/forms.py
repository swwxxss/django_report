from django import forms
from .models import Book
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name', 'book_autor', 'book_genre', 'book_lenguage',
            'book_year_of_public', 'book_price', 'book_article',
            'book_pages', 'book_cover', 'book_photo', 'book_description',
            'book_availability', 'book_publisher'
        ]

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)