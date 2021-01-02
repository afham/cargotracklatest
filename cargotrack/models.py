from django.db import models

# Create your models here.
class Destination(models.Model):
	
	movetype=models.CharField(max_length=100)
	movedate=models.CharField(max_length=100)
	movefrom=models.CharField(max_length=100)
	moveto=models.CharField(max_length=100)
	waytorecieve=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	other=models.CharField(max_length=100)