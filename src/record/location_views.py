from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .form import *


def location_record_list_view(request):
	#list out locations
	#could be search
	qs = LocationRecord.objects.all()
	print(qs)
	template_name = "location/list.html"
	context = {'object_list': qs}
	return render(request, template_name, context)
	return HttpResponse("<h1>List of locations</h1>")


def location_record_create_view(request):
	#ADD location(s)
	#with a form
	qs = LocationRecord.objects.all()
	context = {'object_list': qs}
	template_name = "location/create.html"
	print(request.POST)
	return render(request, template_name, context)


def location_record_detail_view(request,pkey):
	#VIEW one location in detail
	obj_location = get_object_or_404(LocationRecord, pk=pkey)
	template_name = "location/detail.html"
	context = {'object': obj_location}
	print(obj_location)
	return render(request, template_name, context)
	# return HttpResponse("<h1>view one location in detail</h1>")


def location_record_update_view(request,pkey):
	#MODIFY location
	obj_location = get_object_or_404(LocationRecord, pk=pkey)
	form = LocationForm(request.POST or None, instance=obj_location)
	if form.is_valid():
		form.save()
		return redirect("/location/"+str(obj_location.pk)+"/detail")
	template_name = "location/form.html"
	context = {'form':form}
	return render(request, template_name, context)


def location_record_delete_view(request,pkey):
	return HttpResponse("<h1>delete location</h1>")
