from rest_framework import serializers
from .models import *



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookShelfSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = BookShelf
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    bookshelves = BookShelfSerializer(many=True, read_only=True, source='bookshelf_set')
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = '__all__'