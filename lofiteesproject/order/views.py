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
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

from locationprofile.models import locationProfile
from order.models import Order
from orderline.models import OrderLine
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from allshirts.models import allshirts

from django.core.mail import send_mail



# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_order_no_location_profile(request):
    newOrder = Order.objects.create(
        first_name=request.data.get("first_name"),
        last_name=request.data.get("last_name"),
        street=request.data.get("street"),
        street2=request.data.get("street2"),
        state=request.data.get("state"),
        zipcode=request.data.get("zipcode")
    )
    orderlines = request.data.get("lines")
    split_Order_Lines = orderlines.split(",")

    for line in split_Order_Lines:
        shirtID_size = line.split(".")
        OrderLine.objects.create(shirt_id=allshirts.objects.filter(pk=shirtID_size[0])[0] , size=shirtID_size[1], orderID=newOrder)


    recipients = [request.data.get("email")]

    subject = "LofiTees Order Confirmation Email"
    message_for_customer = '''\nThank you for placing an order with us, {}\n
    *This is an auto-generated message.\n
    *Please do not reply as no one will answer'''.format(request.data.get("first_name"))
    message_for_manufacturer = "Hey someone placed an order"
    send_mail(subject, message_for_customer, "ericklofitees@gmail.com" , recipients, True, "ericklofitees@gmail.com", "foremail2020.")
    send_mail(subject, message_for_manufacturer, "ericklofitees@gmail.com" , recipients, True, "ericklofitees@gmail.com", "foremail2020.")
    return Response({"message":"Order Created!"}, status=HTTP_200_OK) 
