import re

from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, BadHeaderError

from .forms import OwnersSubmitForm
from .models import OwnersSubmit

# Create your views here.

def owners(request):
	if request.method == 'GET':
		owners_submit_form = OwnersSubmitForm(request.POST, request.FILES)
		context = {
			'owners_submit_form': owners_submit_form
			}
		return render(request, 'owners/owners.html', context)

	elif request.method == "POST":
		food_truck_name = request.POST.get('food_truck_name', '')
		state = request.POST.get('state', '')

		owner_name = request.POST.get('owner_name', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')

		owners_submit_form = OwnersSubmitForm(request.POST, request.FILES)
		context = {
			'owners_submit_form': owners_submit_form,
			'food_truck_name': food_truck_name,
			'state': state,
			'owner_name': owner_name,
			'email': email,
			'message': message,
			}

		if owners_submit_form.is_valid():
			new_query = owners_submit_form.save()
			new_query.save()
			messages.success(request, "Thank you, your request has been successfully submitted. We'll be in touch shortly.")
			subject = "New food truck listing enquiry"
			from_email = ['hey.getdelicious@gmail.com']
			message = "Food truck name: %s\nState: %s\nOwner name: %s\nEmail: %s\nMessage: %s" % (food_truck_name, state, owner_name, email, message)
			send_mail(subject, message, state, from_email, ['hey.getdelicious@gmail.com'])
			return HttpResponseRedirect("/")
		else:
			messages.error(request, "* fields are required.")
	return render(request, 'owners/owners.html', context)
