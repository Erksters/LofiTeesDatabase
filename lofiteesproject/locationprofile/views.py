from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_202_ACCEPTED
)

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from locationprofile.models import locationProfile
from django.http import JsonResponse

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
@api_view(["GET"])
def get_my_address(request):
    myToken = request.headers['Authorization'].split(' ')[1]
    myUser = Token.objects.all().filter(key=myToken)[0].user
    data = locationProfile.objects.all().filter(my_user=myUser).values(
        "my_user",
        "street",
        "street2",
        "state",
        "zipcode"
    )
    return JsonResponse(list(data), safe=False) 

@csrf_exempt
@api_view(["POST"])
def create_or_update_my_address(request):
    myToken = request.headers['Authorization'].split(' ')[1]
    myUsername = Token.objects.filter(key=myToken)[0].user
    myUser = User.objects.filter(username=myUsername)
    myLocation_profile = myUser.values("locationprofile")

    if myLocation_profile[0]["locationprofile"] == None:
        locationProfile.objects.create(
        myUser[0], 
        street=request.data.get("street"),
        street2=request.data.get("street2"),
        state=request.data.get("state"),
        zipcode=request.data.get("zipcode"))
        return Response({"message":"user Created"}, status=HTTP_201_CREATED)
    else:
        locationProfile.objects.filter(my_user=myUser[0]).update(
            street=request.data.get("street"),
            street2=request.data.get("street2"),
            state=request.data.get("state"),
            zipcode=request.data.get("zipcode")
        )        
        return Response({"mesage":"updated the address"}, status=HTTP_202_ACCEPTED)

    return Response({"message":"Error, Update did not occur"}, status=HTTP_200_OK)
