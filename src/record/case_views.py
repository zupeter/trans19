from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

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
	# return HttpResponse("<h1>create cases</h1>")
	print(request.POST)
	form = CaseForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = CaseForm()
	context = {"form":form}
	template_name = "case/create/create.html"
	return render(request, template_name,context)


def case_record_detail_view(request,case_num):
	#VIEW case
	#get 1 object -> detail view
	#under case details, list all the visits to locaiton
	obj_case = get_object_or_404(CaseRecord, case_number=case_num)
	template_name = "case/detail.html"
	context = {'object_case': obj_case}
	return render(request, template_name, context)


def case_record_update_view(request,case_num):
	#MODIFY case
	obj = get_object_or_404(CaseRecord, case_number=case_num)
	objlink = obj.case_number
	form = CaseForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("/case/"+str(obj.case_number))
	template_name = "case/modify/modify.html"
	context = {'form':form}
	return render(request, template_name, context)


def case_record_delete_view(request,case_num):
	obj = get_object_or_404(CaseRecord, case_number=case_num)
	template_name = "case/delete/delete.html"
	if request.method == "POST":
		obj.delete()
		return redirect("/case")
	context = {'object_case': obj}
	return render(request, template_name, context)
