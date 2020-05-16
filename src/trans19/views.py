from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_page(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return render(request,"intro.html")