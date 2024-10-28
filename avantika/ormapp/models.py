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

