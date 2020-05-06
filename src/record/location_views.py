from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import *

def location_record_list_view(request):
	#list out locations
	#could be search
	return HttpResponse("<h1>List of locations</h1>")


def location_record_create_view(request):
	#ADD location(s)
	#with a form
	return HttpResponse("<h1>create location</h1>")


def location_record_detail_view(request,case_num):
	#VIEW one location in detail
	return HttpResponse("<h1>view one location in detail</h1>")


def location_record_update_view(request,case_num):
	#MODIFY location
	return HttpResponse("<h1>update location</h1>")


def location_record_delete_view(request,case_num):
	return HttpResponse("<h1>delete location</h1>")