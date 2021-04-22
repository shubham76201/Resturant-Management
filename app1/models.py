from django.db import models

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
    name = models.CharField(max_length=122)
    time_slot=models.CharField(max_length=200)
    table_no=models.CharField(max_length=255)
    table_type=models.CharField(max_length=255)
    guest_no=models.CharField(max_length=122)
    
    def __str__(self):
        return self.name