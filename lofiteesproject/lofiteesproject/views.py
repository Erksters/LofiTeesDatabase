
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from django.shortcuts import redirect
from django.http import JsonResponse


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from locationprofile.models import locationProfile

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.core import serializers

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
    my_location_profile = locationProfile.objects.filter(my_user=user)
    return Response({
        'token': token.key,
        "username":username,
        "locationprofile":serializers.serialize('json',list(my_location_profile)
        )},
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
        email = request.data.get("email")
        User.objects.create_user(username, email=email,  password=password)

        data = {'message': "User Was Created"}
        return Response(data, status=HTTP_200_OK)
        # return redirect('http://127.0.0.1:3000/login/')
    
    data = {"message":"Nothing happened"}
    # return Response(data, status=HTTP_200_OK)


'''
Helps the frontend check to see if a user already exists
'''
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def find_similar_username(request, theName):
    print()
    print()
    print()
    print()
    print("HELLO")
    print()
    print()
    querySet = User.objects.filter(username=theName).count()

    if  querySet == 0:
        data={"message": "{} is available.".format(theName)}
        return Response(data, status=HTTP_404_NOT_FOUND)
    
    else:
        data={"message": "We found {}. Please select another username".format(theName)}
        return Response(data, status=HTTP_400_BAD_REQUEST)

    data={"message": "Something went Wrong"}
    return Response(data, status=HTTP_200_OK)
    
    


'''
To help figure out who is signed in with a token.
Otherwise tell frontend that they need one 
'''
@csrf_exempt
@api_view(["POST"])
def whos_token(request):
    myToken = request.headers['Authorization'].split(' ')[1]
    MyUsername = Token.objects.all().filter(key=myToken)[0].user
    MyUser = User.objects.filter(username=MyUsername).values("username", "locationprofile", "order")
    return JsonResponse(list(MyUser), safe=False)

