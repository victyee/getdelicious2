from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

from django_markdown.models import MarkdownField

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
# Create your models here.

STATE_CHOICES = (
	('Victoria', 'Victoria'),
	('New South Wales', 'New South Wales'),
	('South Australia', 'South Australia'),
	('Queensland', 'Queensland'),
	('Western Australia', 'Western Australia'),
	('Australian Capital Territory', 'Australian Capital Territory'),
	('Northern Territory', 'Northern Territory'),
	('Tasmania', 'Tasmania'),
	)


PRICING_MODEL = (
	('guest', 'guest'),
	('hour', 'hour'),
	('serve', 'serve'),
	('minimum spend', 'minimum spend'),
	)


class Product(models.Model):
	# user = models.OneToOneField(User)
	owner_name = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)
	contact_number = models.CharField(max_length=15, null=True, blank=True)
	product_name = models.CharField(max_length=80)
	logo = models.ImageField(upload_to='foodtruck/logo/', null=True, blank=True)
	slogan = models.TextField(max_length=75, null=True, blank=True)
	about_us = models.TextField(max_length=275, null=True, blank=True)
	operating_state = models.CharField(max_length=120, choices=STATE_CHOICES)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(default=now)
	active = models.BooleanField(default=False)
	number = models.IntegerField(default=1, null=True, blank=True)

	def __unicode__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})


class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)

	#pricing
	price_from = models.BooleanField(default=False)
	price_per = models.CharField(max_length=120, choices=PRICING_MODEL)
	price = models.CharField(max_length=120)
	minimum = models.CharField(max_length=120)
	maximum = models.CharField(max_length=120)

	#includes
	included_travel_distance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	maximum_travel_distance = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
	included_service_hours = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)
	max_service_hours = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)

	#additional
	extra_km_not_available = models.BooleanField(default=False)
	extra_hours_not_available = models.BooleanField(default=False)
	extra_km_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
	extra_hours_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
	please_call_to_discuss = models.BooleanField(default=False)

	#dietary
	gluten_free_options_upon_request = models.BooleanField(default=False)
	vegetarian_options_upon_request= models.BooleanField(default=False)

	number = models.IntegerField(default=1, null=True, blank=True)
	menu = MarkdownField(max_length=2000)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def spaceless_title(self):
		title = self.title
		spaceless = title.replace(" ", "").replace("\'", "").replace("/", "").replace("+", "").replace(",", "").replace("&", "and")
		return spaceless