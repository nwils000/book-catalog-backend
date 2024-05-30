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
    )
    profile.save()

    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_all_profile_info(request):
#     profile = request.user.profile
#     bookshelves = profile.bookshelf_set.all()
#     serialized_profile = ProfileSerializer(profile)
#     serialized_bookshelves = BookShelfSerializer(bookshelves, many=True)

#     response_structure = {
#         'profile': serialized_profile.data,
#         'bookshelves': serialized_bookshelves.data
#     }

#     return Response(response_structure)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer