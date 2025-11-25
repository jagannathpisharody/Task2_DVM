from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ticket(models.Model):
	passenger = models.ForeignKey(User, on_delete=models.CASCADE)
	startID = models.IntegerField(default = None)
	endID = models.IntegerField(default = None)
	purchaseDate = models.DateTimeField(default=timezone.now)
	travelDate = models.DateTimeField()

class Station(models.Model):
	uID = models.IntegerField()
	Name = models.CharField(max_length = 30)
	LineID = models.IntegerField(default = None)
	LineInterchangeID = models.IntegerField(default = None)



