# Ex01 Django ORM Web Application
## Date: 26.11.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
model.py
from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=20, help_text="Enter Student Name")
    age = models.IntegerField(help_text="Enter age between 18 to 22")
    dob = models.DateField()
    reg_no = models.IntegerField(help_text="Enter the Register Number")

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'age', 'dob', 'reg_no']

admin.py
from django.contrib import admin

# Register your models here.
from .models import Student, StudentAdmin
# Register your models here.
admin.site.register(Student, StudentAdmin)
```
## OUTPUT
<img width="1024" height="585" alt="image" src="https://github.com/user-attachments/assets/2345cead-6eca-4850-a6b0-e64ae83cf359" />
<img width="1911" height="993" alt="image" src="https://github.com/user-attachments/assets/409194da-4f35-4b43-9198-d0c2367c7721" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1a712f7b-56c7-4e9b-9aff-dc1e07588220" />



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
