from django.db import models
from django.contrib.auth.models import User

GENRES = (
    ('FICTION', 'Fiction'),
    ('NONFICTION', 'Non-Fiction'),
    ('MYSTERY', 'Mystery'),
    ('THRILLER', 'Thriller'),
    ('HORROR', 'Horror'),
    ('SCI-FI', 'Science Fiction'),
    ('FANTASY', 'Fantasy'),
    ('ROMANCE', 'Romance'),
    ('BIOGRAPHY', 'Biography'),
    ('POETRY', 'Poetry'),
    ('HISTORICAL', 'Historical'),
    ('SELF_HELP', 'Self Help'),
    ('CHILDREN', 'Children’s'),
    ('YOUNG_ADULT', 'Young Adult'),
    ('EDUCATION', 'Education'),
    ('COMIC', 'Comic Book'),
    ('GRAPHIC_NOVEL', 'Graphic Novel'),
    ('BUSINESS', 'Business'),
    ('TECHNOLOGY', 'Technology'),
    ('COOKING', 'Cooking'),
    ('TRAVEL', 'Travel'),
    ('RELIGION', 'Religion'),
    ('TRUE_CRIME', 'True Crime'),
    ('SPORTS', 'Sports'),
    ('MUSIC', 'Music'),
    ('ART', 'Art'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    
class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=50, choices=GENRES)
    description = models.TextField()

    def __str__(self):
        return self.title

class BookShelf(models.Model):
    title = models.CharField(max_length=100, default='Book Shelf')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.owner.user.username}s bookshelf'