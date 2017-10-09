#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import App

def index(request):
	all_apps = App.objects.all()
	html = '<h1>This is the list of available apps</h1>'
	for app in all_apps:
		url = '/appstore/' + str(app.id) + '/'
		html += '<li><a href="' + url + '">' + app.name + '</a></li>'
	return HttpResponse(html)


def detail(request, app_id):
	return HttpResponse('<h2>Details for app ' + str(app_id) + '</h2>')

 