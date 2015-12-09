from django.contrib import admin
from .models import BlogPost, BlogPicture
# Register your models here.


class BlogPictureInline(admin.StackedInline):
    model = BlogPicture
    extra = 0


class BlogPostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ["title", "updated"]
	ordering = ['-timestamp']
	class Meta:
		model = BlogPost

	inlines = [BlogPictureInline]

admin.site.register(BlogPost, BlogPostAdmin)

