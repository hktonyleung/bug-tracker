from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# Create your views here.
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Username/Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

@api_view(["PUT"])
def update(request):
    new_username = request.data.get("new_username")
    if new_username is None:
        return Response({'error': 'Please provide new username'},
                        status=status.HTTP_400_BAD_REQUEST)
    User = get_user_model()


    #TODO: Check whether new username was used and return error

    #Catch the integrity error in case new username was used
    try:
        user = User.objects.get(id=request.user.pk)
        user.username = new_username
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except IntegrityError:
        return Response({'error': 'The username was used. Please select another one'},
            status=status.HTTP_400_BAD_REQUEST)



