from django.db import models
from django.contrib import admin
from .models import HitCount

# Register your models here.

class HitCountAdmin(admin.ModelAdmin):
	list_display = ('food_truck', 'url', 'hits')
	list_filter = ('food_truck', 'hits')
	search_fields = ['url']

admin.site.register(HitCount, HitCountAdmin)