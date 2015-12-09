from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


class OwnersSubmit(models.Model):
	#food truck details
	food_truck_name = models.CharField(max_length=200)
	state = models.CharField(max_length=100)

	#owner's details
	owner_name = models.CharField(max_length=150)
	email = models.EmailField(max_length=200)
	message = models.TextField(max_length=1000, null=True, blank=True)

	def __unicode__(self):
		return self.food_truck_name

