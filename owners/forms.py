from django import forms

from .models import OwnersSubmit

class OwnersSubmitForm(forms.ModelForm):
	class Meta:
		model = OwnersSubmit
		fields = ["food_truck_name",
				"state",
				"owner_name",
				"email",
				"message",
				]