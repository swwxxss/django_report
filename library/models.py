from django.db import models
from django import forms
from django.contrib.auth.models import User


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_autor = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=100)
    book_lenguage = models.CharField(max_length=30)
    book_year_of_public = models.IntegerField()
    book_publisher = models.CharField(max_length=100, default="unknown")
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_article = models.CharField(max_length=10)
    book_pages = models.IntegerField()
    book_cover = models.CharField(max_length=100) # add options
    book_description = models.TextField()
    book_availability = models.BooleanField(default=True)
    book_photo = models.ImageField(upload_to='photos/', default='default.jpg')

    def __str__(self):
        return self.book_name


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=3, blank=True)


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.first_name} {self.last_name}"