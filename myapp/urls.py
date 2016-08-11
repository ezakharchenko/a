from django.conf.urls import url


from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view(), name='client-list'),
    url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view(), name='client-detail'),
    url(r'^clients/create/$', views.ClientCreate.as_view(), name='client-create'),
    url(r'^clients/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(success_url = "/myapp/clients/"), name='client-delete'),

]

"""
url(r'^clients/delete/$', views.ClientDelete.as_view(), name='client-delete'),
url(r'^clients/(?P<pk>[0-9]+)/$', views.ClientUpdate.as_view(), name='client-update'),
"""