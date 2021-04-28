from django.db import models
from django.db.models import Model

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=122)
    first_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class Book_table(models.Model):
    booking_id=models.IntegerField()
    name = models.CharField(max_length=122)
    time_slot=models.CharField(max_length=200)
    table_no=models.CharField(max_length=255)
    table_type=models.CharField(max_length=200)
    guest_no=models.CharField(max_length=255)
    date=models.DateField(max_length=255)

    
    def __str__(self):
        return self.name

class Order_Now(models.Model):
    image=models.URLField()
    name = models.CharField(max_length=255)
    gmail=models.EmailField(max_length=220)
    order_id=models.IntegerField(unique=True)
    distance_from_home=models.FloatField()
    Order_Snacks=models.CharField(max_length=255)
    Order_lunch=models.CharField(max_length=255)
    Order_Beverages=models.CharField(max_length=200)
    date1=models.DateField(max_length=255)
    takeaway=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name



    
    