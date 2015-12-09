from django.shortcuts import render
import markdown

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogPost, BlogPicture
# Create your views here.

def ideas(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    template = 'blog/home.html'
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        blogpost = paginator.page(page)
    except PageNotAnInteger:
        blogpost = paginator.page(1)
    except EmptyPage:
        blogpost = paginator.page(paginator.num_pages)

    context = { 'posts': posts, 'blogpost': blogpost, }
    return render(request, template, context)


def post(request, slug):
    user = request.user
    post = BlogPost.objects.get(slug=slug)
    template = 'blog/post.html'

    context = {
            'user': user,
            'post': post,
    }
    return render(request, template, context)

