from django import forms


class ClientForm(forms.Form):
	
	first_name = forms.CharField()
	last_name = forms.CharField()
	address_1 = forms.CharField()
	address_2 = forms.CharField()
	phone = forms.CharField()
	date_created = forms.DateTimeField()

class AppointmentForm(forms.Form):

	appointment_text = forms.CharField()
	appointment_date = forms.DateTimeField()
	code_1 = forms.CharField()
	code_2 = forms.CharField()
