from django.shortcuts import render
import random
from .models import Product, Variation
from quotes.models import Quote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def single(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    packages = product.variation_set.all().order_by('number')

    page_title = 'Seriously Delicious Food Truck Catering with %s | getdelicious.com.au' % (product.product_name.title())

    template = 'products/single.html'
    context = {
            'product': product,
            'packages': packages,
            'page_title': page_title,
    }
    return render(request, template, context)


def victoria(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	page_title = "Food trucks catering in Melbourne, Victoria | getdelicious.com.au"
	state = "Victoria"
	trucks = Product.objects.filter(operating_state="Victoria").order_by('number')

	paginator = Paginator(trucks, 9)
	page = request.GET.get('page')
	try:
		foodtrucks = paginator.page(page)
	except PageNotAnInteger:
		foodtrucks = paginator.page(1)
	except EmptyPage:
		foodtrucks = paginator.page(paginator.num_pages)

	template = 'products/state_results.html'
	context = {"state": state,
				"quote": quote,
				"trucks": trucks,
				"page_title": page_title,
				"foodtrucks": foodtrucks,
			}
	return render(request, template, context)


def south_australia(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	page_title = "Food trucks catering in Adelaide, South Australia | getdelicious.com.au"
	state = "South Australia"
	trucks = Product.objects.filter(operating_state="South Australia").order_by('number')

	paginator = Paginator(trucks, 9)
	page = request.GET.get('page')
	try:
		foodtrucks = paginator.page(page)
	except PageNotAnInteger:
		foodtrucks = paginator.page(1)
	except EmptyPage:
		foodtrucks = paginator.page(paginator.num_pages)

	template = 'products/state_results.html'
	context = {"state": state,
				"quote": quote,
				"trucks": trucks,
				"page_title": page_title,
				"foodtrucks": foodtrucks,
			}
	return render(request, template, context)



def western_australia(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	page_title = "Food trucks catering in Perth, Western Australia | getdelicious.com.au"
	state = "Western Australia"
	trucks = Product.objects.filter(operating_state="Western Australia").order_by('number')

	paginator = Paginator(trucks, 9)
	page = request.GET.get('page')
	try:
		foodtrucks = paginator.page(page)
	except PageNotAnInteger:
		foodtrucks = paginator.page(1)
	except EmptyPage:
		foodtrucks = paginator.page(paginator.num_pages)

	template = 'products/state_results.html'
	context = {"state": state,
				"quote": quote,
				"trucks": trucks,
				"page_title": page_title,
				"foodtrucks": foodtrucks,
			}
	return render(request, template, context)



def new_south_wales(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	page_title = "Food trucks catering in Sydney, New South Wales | getdelicious.com.au"
	state = "New South Wales"
	trucks = Product.objects.filter(operating_state="New South Wales").order_by('number')

	paginator = Paginator(trucks, 9)
	page = request.GET.get('page')
	try:
		foodtrucks = paginator.page(page)
	except PageNotAnInteger:
		foodtrucks = paginator.page(1)
	except EmptyPage:
		foodtrucks = paginator.page(paginator.num_pages)

	template = 'products/state_results.html'
	context = {"state": state,
				"quote": quote,
				"trucks": trucks,
				"page_title": page_title,
				"foodtrucks": foodtrucks,
			}
	return render(request, template, context)


def queensland(request):
	quotes = Quote.objects.all()
	quote = random.choice(quotes)
	page_title = "Food trucks catering in Brisbane, Queensland | getdelicious.com.au"
	state = "Queensland"
	trucks = Product.objects.filter(operating_state="Queensland").order_by('number')

	paginator = Paginator(trucks, 9)
	page = request.GET.get('page')
	try:
		foodtrucks = paginator.page(page)
	except PageNotAnInteger:
		foodtrucks = paginator.page(1)
	except EmptyPage:
		foodtrucks = paginator.page(paginator.num_pages)

	template = 'products/state_results.html'
	context = {"state": state,
				"quote": quote,
				"trucks": trucks,
				"page_title": page_title,
				"foodtrucks": foodtrucks,
			}
	return render(request, template, context)
