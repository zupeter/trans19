from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

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
	qs = CaseRecord.objects.all()
	template_name = "case/create/create.html"
	context = {'object_list': qs}
	return render(request, template_name, context)


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
	return HttpResponse("<h1>update case</h1>")


def case_record_delete_view(request,case_num):
	return HttpResponse("<h1>delete case</h1>")
