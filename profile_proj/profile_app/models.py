from django.db import models

# Create your models here.


class myprofile(models.Model):
    name=models.CharField( max_length=50)
    father_name=models.CharField( max_length=50)
    mother_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=54)
    roll_no=models.IntegerField()
    stream=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    pin_code=models.CharField( max_length=6)
    gender=models.CharField( max_length=50)
    mobile_no=models.CharField( max_length=10)
    image=models.ImageField(upload_to='media')
    description=models.CharField(max_length=400)