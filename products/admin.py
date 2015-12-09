from django.contrib import admin

# Register your models here.
from .models import Product, Variation


class VariationInline(admin.StackedInline):
	model = Variation
	extra = 0
	ordering = ["number"]



class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_name", "operating_state", "number"]
	prepopulated_fields = {"slug": ("product_name",)}
	list_editable = ["number"]
	class Meta:
		model = Variation

	inlines = [VariationInline]
	

admin.site.register(Product, ProductAdmin)