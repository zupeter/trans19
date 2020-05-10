from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .form import *


def location_record_list_view(request):
	#list out locations
	#could be search
	qs = LocationRecord.objects.all()
	template_name = "location/list.html"
	context = {'object_list': qs}
	return render(request, template_name, context)
	return HttpResponse("<h1>List of locations</h1>")


def location_record_create_view(request):
	#ADD location(s)
	#with a form
	form = LocationForm(request.POST or None)
	context = {'form':form}
	template_name = "location/create.html"

	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = LocationForm()
		context = {'form':form, 'saved':True}
	return render(request, template_name, context)


def location_record_detail_view(request,pkey):
	#VIEW one location in detail
	obj_location = get_object_or_404(LocationRecord, pk=pkey)
	template_name = "location/detail.html"
	context = {'object': obj_location}
	return render(request, template_name, context)
	# return HttpResponse("<h1>view one location in detail</h1>")


def location_record_update_view(request,pkey):
	#MODIFY location
	obj_location = get_object_or_404(LocationRecord, pk=pkey)
	form = LocationForm(request.POST or None, instance=obj_location)
	template_name = "location/form.html"
	context = {'form':form}
	if form.is_valid():
		form.save()
		context = {'form':form, 'saved':True}
	return render(request, template_name, context)


def location_record_delete_view(request,pkey):
	obj = get_object_or_404(LocationRecord, pk=pkey)
	template_name = "location/delete.html"
	if request.method == "POST":
		obj.delete()
		return redirect("/location")
	context = {'object': obj}
	return render(request, template_name, context)
