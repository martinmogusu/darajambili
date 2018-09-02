from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('c2b/validation', views.c2b_validation, name='c2b_validation'),
	path('c2b/confirmation', views.c2b_confirmation, name='c2b_confirmation'),
]