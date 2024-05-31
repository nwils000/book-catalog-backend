from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework import viewsets
from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    print('request', request)
    serialized_profile = ProfileSerializer(request.user.profile)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request): 
    user = User.objects.create(username=request.data['username'])
    user.set_password(request.data['password']) 
    user.save()

    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
        # username=request.data['username']
    )
    profile.save()

    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_create_book(request): 
    book = Book.objects.create(title=request.data['title'], author=request.data['author'], description=request.data['description'], genre=request.data['genre'])
    book.save()
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'})
    except Profile.DoesNotExist:
        return Response({'error': 'Profile does not exist'})
    

    bookshelf = BookShelf.objects.get(owner=profile, title=request.data['shelf_title']['shelf_title'])

    bookshelf.books.add(book)

    book_serialized = BookSerializer(book)
    return Response(book_serialized.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_create_bookshelf(request): 
    try:
        user = user = request.user
        profile = Profile.objects.get(user=user)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'})
    except Profile.DoesNotExist:
        return Response({'error': 'Profile does not exist'})

    bookshelf = BookShelf.objects.create(owner=profile, title=request.data['title'])

    bookshelf_serialized = BookShelfSerializer(bookshelf)
    return Response(bookshelf_serialized.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def delete_book_from_shelf(request):
    try:
        user = request.user
        profile = Profile.objects.get(user=user)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'})
    except Profile.DoesNotExist:
        return Response({'error': 'Profile does not exist'})
    try:
        book = Book.objects.get(title=request.data['title'], author=request.data['author'])
        book.save()
    except Book.DoesNotExist:
        return Response({'error': 'Book does not exist'})

    bookshelf, created = BookShelf.objects.get_or_create(owner=profile, title=request.data['shelf_title'])

    bookshelf.books.remove(book)
    bookshelf.save()

    bookshelf_serialized = BookShelfSerializer(bookshelf)
    return Response(bookshelf_serialized.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request):
    user = request.user
    # profile = Profile.objects.get(user=user)
    user = User.objects.get(username=request.user.username)
    book = Book.objects.get(title=request.data['prev_title'])

    data = request.data.copy()
    data.pop('prev_title', None) 

    book_serialized = BookSerializer(book, data=request.data)
    if book_serialized.is_valid():
        book_serialized.save()
        return Response(book_serialized.data)
    else:
        return Response(book_serialized.errors)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer