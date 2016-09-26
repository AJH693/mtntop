from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
	template = loader.get_template('peak/index.html')
	context = {}
	# render(request, 'polls/index.html', context)
	return HttpResponse(template.render(context, request))

def about_me(request):
	return HttpResponse("This is my page")

def portfolio(request):
	return HttpResponse("This is my portfolio")

def contact(request):
	return HttpResponse("Contact Me!")