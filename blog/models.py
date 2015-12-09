from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from django.utils.timezone import now
# Create your models here.

class BlogPost(models.Model):
	user = models.CharField(max_length=250, default='getdelicious')
	title = models.CharField(max_length=350)
	subtitle = models.CharField(max_length=350, blank=True, null=True)
	post = MarkdownField(max_length=200000)
	coverpicture = models.ImageField(upload_to='blog/coverpicture/', null=True, blank=True)
	number = models.IntegerField(null=True, blank=True)
	slug = models.SlugField(unique=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(default=now)

	class Meta:
		ordering = ['timestamp']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("single_post", kwargs={"slug": self.slug})


class BlogPicture(models.Model):
	post = models.ForeignKey(BlogPost)
	image = models.ImageField(upload_to='blog/post_images/')
	number = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.post.title