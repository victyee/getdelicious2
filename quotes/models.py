from django.db import models

# Create your models here.


class Quote(models.Model):
	line = models.TextField(max_length=1200)

	def __unicode__(self):
		return self.line