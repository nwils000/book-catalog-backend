# Generated by Django 5.0.6 on 2024-05-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_books', '0006_bookshelf_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]