from django.db import models
from django.contrib.auth.models import User
from allshirts.models import allshirts
# Create your models here.
class Order(models.Model): 
    my_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length = 50, default="") 
    last_name = models.CharField(max_length = 50, default="") 
    street = models.CharField(max_length = 200, default="") 
    street2 = models.CharField(max_length = 15, default="") 
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 10) 
    date_created = models.DateTimeField(auto_now_add = True) 
    paypal_id = models.CharField(max_length = 200, null=True, blank = True)
    def __str__(self):
        return '%s' % (self.pk)