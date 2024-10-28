# Ex02 Django ORM Web Application
## Date: 28/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Alt text](<Screenshot (14).png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
	Name=models.CharField(max_length=50)
	Accountno=models.IntegerField(primary_key="accno")
	Amount=models.IntegerField()
	Interest=models.FloatField()
	Startdate=models.DateField()
	mobileno=models.IntegerField()
	Enddate=models.DateField()
	
class BankloanAdmin(admin.ModelAdmin):
	list_display=('Name','Accountno','Amount','Interest','Startdate','mobileno','Enddate')

admin.py

from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```


## OUTPUT
![Alt text](<Screenshot (15).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
