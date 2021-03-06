"""lofiteesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf.urls.static import static
from .views import login, sign_up, find_similar_username, whos_token, logout
from allshirts.views import get_all_shirts, get_shirt, get_shirt_by_id
from locationprofile.views import get_my_address, create_or_update_my_address
from order.views import create_order_no_location_profile, fetch_my_orders, fetch_my_orderlines
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login',login),
    path('api/sign_up', sign_up),
    path('api/find_similar_username/<slug:theName>', find_similar_username),
    path('api/whos_token', whos_token),
    path('api/logout', logout),
    path('api/create_order_no_location_profile', create_order_no_location_profile),
    path('api/fetch_my_orders', fetch_my_orders),
    path('api/fetch_my_orderlines', fetch_my_orderlines),
    path('api/allshirts', get_all_shirts ),
    path('api/get_shirt/<str:title>', get_shirt),
    path('api/get_shirt_by_id/<str:id>', get_shirt_by_id),
    path('api/my_address',get_my_address ),
    path('api/create_or_update_my_address',create_or_update_my_address )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
