from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_autor', 'book_genre', 'book_lenuage', 'book_year_of_public', 'book_price', 'book_pages', 'book_availability', 'book_cover', 'book_article', 'book_description')
    search_fields = ('book_name', 'book_autor')

admin.site.register(Book)
