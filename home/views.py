from django.shortcuts import render
import random
from quotes.models import Quote

# Create your views here.

def home(request):
	user = request.user
	template = 'home/home.html'
	context = {}
	return render(request, template, context)


def about(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	context = {
		'quote': quote,
	}
	return render(request, 'home/about.html', context)

def ideas(request):
	context = {}
	return render(request, 'home/ideas.html', context)

def faq(request):
	context = {}
	return render(request, 'home/faq.html', context)

def privacy(request):
	context = {}
	return render(request, 'home/privacy.html', context)

def terms(request):
	context = {}
	return render(request, 'home/terms.html', context)

