# Generated by Django 5.0 on 2024-10-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_book_photo_book_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
