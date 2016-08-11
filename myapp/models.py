from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Client(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address_1 = models.CharField(max_length=200)
	address_2 = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	date_created = models.DateTimeField(default=timezone.now())
	
	def __str__(self):
		return self.first_name
	def __str__(self):
		return self.last_name
	def __str__(self):
		return self.address_1
	def __str__(self):
		return self.address_2
	def __str__(self):
		return self.phone	
	def get_absolute_url(self):
		return "/myapp/clients/"


	

@python_2_unicode_compatible
class Appointment(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	appointment_text = models.CharField(max_length=200)
	appointment_date = models.DateTimeField('appointment date')
	code_1 = models.IntegerField(default='0')
	code_2 = models.IntegerField(default='0')
	
	def __str__(self):
		return self.appointment_text


"""
def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def get_absolute_url(self):
		return "/myapp/clients/"
	def time(self):
		date_created = timezone.now()
		return self.date_created 
"""