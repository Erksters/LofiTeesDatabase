from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class locationProfile(models.Model): 
    # fields of the model 
    my_user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length = 200) 
    street2 = models.CharField(max_length = 15, default="") 
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 10) 
  
    def __str__(self): 
        return self.state 