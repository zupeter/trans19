from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import *

def case_record_list_view(request):
	#list out cases
	#could be search
	return HttpResponse("<h1>List of cases</h1>")


def case_record_create_view(request):
	#ADD case(s)
	#with a form
	return HttpResponse("<h1>create cases</h1>")


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