from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'website/index.html')

def tour(request):
	return HttpResponse("Welcome to the tours page")
