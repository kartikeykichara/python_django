from django.db import models

# Create your models here.

# orm convert pyhton code into sql code(object relational mapper) by migrate command


class student_details(models.Model):
    username =models.CharField(max_length=50)
    email =models.EmailField(max_length=60)
    address =models.CharField(max_length=100)
    city =models.CharField(max_length=20)
    state =models.CharField(max_length=20)
    pin_code =models.IntegerField()
        
        

class student(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    mobile_no=models.IntegerField(max_length=10)
    pin_code=models.IntegerField(max_length=10)
    
    
    