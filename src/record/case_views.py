from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .form import *

# CRUD #Create / Retrieve / Update / Delete

# GET ->Retrieve / List

# POST -> Create / Update / Delete


def case_record_list_view(request):
	#list out cases
	#could be search
	qs = CaseRecord.objects.all()
	template_name = "case/list.html"
	context = {'object_list': qs}
	return render(request, template_name, context)


def case_record_create_view(request):
	# MANSOOOOOOOOOOOOOOOON HI
	#ADD case(s)
	#with a form
	form = CaseForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		# obj.case_num
		obj.save()
		form = CaseForm()
	context = {"form":form}
	template_name = "case/create/create.html"
	return render(request, template_name,context)


def case_record_detail_view(request, pkey):
	#VIEW case
	#get 1 object -> detail view
	#under case details, list all the visits to location
	obj_case = get_object_or_404(CaseRecord, pk=pkey)
	template_name = "case/detail.html"
	context = {'object_case': obj_case}
	return render(request, template_name, context)


def case_record_update_view(request, pkey):
	#MODIFY case

	obj = get_object_or_404(CaseRecord, pk=pkey)
	objlink = obj.case_number
	form = CaseForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("/case/"+str(obj.case_number))
	template_name = "case/modify/modify.html"
	context = {'form':form}

	return render(request, template_name, context)


def case_record_delete_view(request, pkey):
	obj = get_object_or_404(CaseRecord, pk=pkey)
	template_name = "case/delete/delete.html"
	if request.method == "POST":
		obj.delete()
		return redirect("/case")
	context = {'object_case': obj}
	return render(request, template_name, context)


def case_record_add_visit_view(request, pkey):
	form = VisitForm(request.POST or None)
	obj_case = get_object_or_404(CaseRecord, pk=pkey)
	template_name = "Visit/form.html"

	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = VisitForm()

	context = {"form":form}
	template_name = "Visit/form.html"
	return render(request, template_name,context)


def case_record_modify_visit_view(request, pkey, vpkey):
	obj_case = get_object_or_404(CaseRecord, pk=pkey)
	obj_visit = get_object_or_404(VisitRecord, pk=vpkey)
	form = VisitForm(request.POST or None, instance=obj_visit)
	if form.is_valid():
		form.save()
		return redirect("../..")
	template_name = "Visit/edit.html"
	context = {'form':form, 'case':obj_case, 'visit':obj_visit}
	return render(request, template_name, context)


def case_record_delete_visit_view(request, pkey, vpkey):
	obj_case = get_object_or_404(CaseRecord, pk=pkey)
	obj_visit = get_object_or_404(VisitRecord, pk=vpkey)
	if request.method == "POST":
		obj_visit.delete()
		return redirect("/case/"+str(pkey))
	context = {'case':obj_case,'visit':obj_visit}
	template_name = "Visit/delete.html"
	return render(request, template_name, context)

def case_search_connections(request, pkey, vpkey):
	obj_case = get_object_or_404(CaseRecord, pk=pkey)
	obj_visit = get_object_or_404(VisitRecord, pk=vpkey)
	# connection_visit = VisitRecord.objects.filter(~Q(date_from > obj_visit.date_to +2), ~Q(date_from < obj_visit.date_from -2),Q(location = obj_visit.location))
	# connection_case = get_object_or_404(CaseRecord, case_number = connection_visit.case) #someone help me link them together
	# context = {'og_case':obj_case,'og_visit':obj_visit, 'connection_case':connection_case, 'connection_visit':connection_visit}
	form = SearchForm(request.POST or None)
	connections = []
	if form.is_valid():
		print (form.cleaned_data['window'])
		print (obj_visit.location)
		print (obj_visit.location.visitrecord_set.all())
		for visit in obj_visit.location.visitrecord_set.all():
			print (visit)
	context = {'selected_case':obj_case,'selected_visit':obj_visit, 'form':form, 'conn':connections}
	template_name = "case/connections.html"
	return render(request, template_name, context)
