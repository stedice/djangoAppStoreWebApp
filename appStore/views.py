from django.http import HttpResponse
from django.shortcuts import render
from .models import App


def index(request):
	context = {'all_apps': App.objects.all()}
	return render(request, 'appStore/index.html' , context )

def detail(request, app_id):
	return HttpResponse('<h2>Details for app ' + str(app_id) + '</h2>')

   