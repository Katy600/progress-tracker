from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^search/$', views.search),
	url(r'^struggles/$', views.add_struggle),
]
