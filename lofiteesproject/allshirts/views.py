from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.core import serializers
from allshirts.models import allshirts

from django.http import JsonResponse


# Create your views here.
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_shirts(request):
    data = allshirts.objects.all().values(
        "title",
        "date_created",
        "img",
        "description"
    )
    datalist = list(data)
    return JsonResponse(datalist, safe=False) 


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_shirt(request, title):
    data = allshirts.objects.all().filter(title=title).values(
        "title",
        "date_created",
        "img",
        "description",
        "pk"
    )
    datalist = list(data)
    return JsonResponse(datalist, safe=False) 



@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_shirt_by_id(request, id):
    data = allshirts.objects.all().filter(pk=id).values(
        "title",
        "date_created",
        "img",
        "description",
        "pk"
    )
    datalist = list(data)
    return JsonResponse(datalist, safe=False) 