# Generated by Django 5.0.6 on 2024-05-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_books', '0005_alter_book_genre_delete_totalbookcatalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='title',
            field=models.CharField(default='Book Shelf', max_length=100),
        ),
    ]
