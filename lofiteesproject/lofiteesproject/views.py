
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.contrib.auth.models import User

from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response

'''
Checks for valid User authentication and will
 generate a new Token for their use of the site
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username") 
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

'''
Checks for valid token and will sign out a user
 removing their access from the other api endpoints 
'''
@csrf_exempt
@api_view(["POST"])
def logout(request):
    myToken = request.headers['Authorization'].split(' ')[1]
    Token.objects.all().filter(key=myToken).delete()
    data = {"message":"token deleted"}
    return Response(data, status=HTTP_200_OK)


'''
To sign a new user up with a username, password, and email
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def sign_up(request):
    if request.method == "POST":

        username = request.data.get("username") 
        password = request.data.get("password")


        data = {'message': "User Was Created"}
        User.objects.create_user(username, email="someemail@email.com",  password=password)
        # User.objects.create_user(username='username', password='ROYGBIabc123.', email="someemail@email.com")
        return Response(data, status=HTTP_200_OK)

    # return redirect('http://127.0.0.1:3000/login/')
    # return redirect('http://google.com/')


'''
Helps the frontend check to see if a user already exists
'''
@csrf_exempt
@permission_classes((AllowAny,))
def find_similar_username(request, theName):
    print(request)
    querySet = User.objects.filter(username=theName).count()
    if  querySet == 0:
        data={"message": "{} is available.".format(theName)}
        return Response(data, status=HTTP_404_NOT_FOUND)
    
    else:
        data={"message": "We found {}. Please select another username".format(theName)}
        return Response(data, status=HTTP_400_BAD_REQUEST)


'''
To help figure out who is signed in with a token.
Otherwise tell frontend that they need one 
'''
@csrf_exempt
@api_view(["POST"])
def whos_token(request):
    myToken = request.headers['Authorization'].split(' ')[1]
    data ={"myUser": serializers.serialize("json",Token.objects.all().filter(key=myToken) )} 
    return Response(data, status=HTTP_200_OK)



# def my_orders(request, userID):