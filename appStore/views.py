from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import App


def index(request):
	context = {'all_apps': App.objects.all()}
	return render(request, 'appStore/index.html' , context )

def detail(request, app_id):
	try:
		app = App.objects.get(pk = app_id)
	except App.DoesNotExist:
		raise Http404("App does not exist")
	return render(request, 'appStore/detail.html' , {'app': app} )

     