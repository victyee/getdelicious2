from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from products.models import Product
from blog.models import BlogPost

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'victoria', 'south_australia', 'western_australia', 'about', 'faq', 'contact', 'owners', 'ideas']

    def location(self, item):
        return reverse(item)


class ProductsViewSitemap(sitemaps.Sitemap):
	changefreq = 'daily'
	priority = 1.0

	def items(self):
		return Product.objects.all()


class BlogPostsViewSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return BlogPost.objects.all()

