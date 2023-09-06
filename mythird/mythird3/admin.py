from django.contrib import admin
from .models import student_details
from .models import student
# Register your models here.

admin.site.register(student_details)


admin.site.register(student)