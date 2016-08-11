from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.forms import ModelForm
from myapp.models import Client
from myapp.forms import ClientForm
from django.utils import timezone


class ClientCreate(CreateView):
	model = Client
	success_url = ''
	fields = ['first_name', 'last_name']
	template_name = 'myapp/client-create.html'
	
class ClientDelete(DeleteView):
    model = Client
    template_name = 'myapp/client-delete.html'


class ClientList(ListView):
	model = Client
	template_name = 'myapp/client-list.html'
	context_object_name = 'latest_client_list'

	def get_queryset(self):
		return Client.objects.order_by('last_name')

class ClientDetail(DetailView):
	queryset = Client.objects.all()
	template_name = 'myapp/client-detail.html'

"""
def get_object(self):
	        # Call the superclass
	        object = super(ClientCreateView, self).get_object()
	        # Record the last accessed date
	        object.date_created = timezone.now()
	        object.save()
	        # Return the object
	        return object
"""	    	   