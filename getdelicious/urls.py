from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from products import views
from contact import views
from blog import views
from home import views
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ProductsViewSitemap, BlogPostsViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductsViewSitemap,
    'blogpost': BlogPostsViewSitemap,
}

urlpatterns = patterns('',
    url(r'^batcave/', include(admin.site.urls)),

    #homepage
    url(r'^$', 'home.views.home', name='home'),

    #states
    url(r'^food-trucks-victoria/$', 'products.views.victoria', name='victoria'),
    url(r'^food-trucks-south-australia/$', 'products.views.south_australia', name='south_australia'),
    url(r'^food-trucks-western-australia/$', 'products.views.western_australia', name='western_australia'),
    url(r'^food-trucks-new-south-wales/$', 'products.views.new_south_wales', name='new_south_wales'),    
    url(r'^food-trucks-queensland/$', 'products.views.queensland', name='queensland'),

    #nav pages
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^faq/$', 'home.views.faq', name='faq'),
    url(r'^privacy/$', 'home.views.privacy', name='privacy'),
    url(r'^terms/$', 'home.views.terms', name='terms'),

    #ideas
    url(r'^ideas/$', 'blog.views.ideas', name='ideas'),

    #contact
    url(r'^contact/$', 'contact.views.contact', name='contact'),

    # owners page
    url(r'^owners/$', 'owners.views.owners', name='owners'),
    
    #markdown
    url(r'^markdown/', include("django_markdown.urls")),

    #sitemaps
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    #blog page views
    url(r'^ideas/(?P<slug>[\w-]+)/$', 'blog.views.post', name='single_post'),

    #food truck page views
    url(r'^(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


if settings.DEBUG:
    handler404 = 'views.custom_404'
    handler500 = 'views.custom_500'