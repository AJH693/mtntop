from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("hello, world. You're at the peak index.")

def about_me(request):
	return HttpResponse("This is my page")

def portfolio(request):
	return HttpResponse("This is my portfolio")

def contact(request):
	return HttpResponse("Contact Me!")