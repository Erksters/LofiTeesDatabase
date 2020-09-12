from django.db import models
from order.models import Order
from allshirts.models import allshirts

# Create your models here.
class OrderLine(models.Model): 
    size = models.CharField(max_length=5)
    shirt_id = models.ForeignKey(allshirts, on_delete=models.CASCADE, null=False)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    refund = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s' % (self.pk)





    
    