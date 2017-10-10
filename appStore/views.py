from django.shortcuts import render, get_object_or_404
from .models import App


def index(request):
	context = {'all_apps': App.objects.all()}
	return render(request, 'appStore/index.html' , context )

def detail(request, app_id):
	app = get_object_or_404(App, pk = app_id)
	platform = app.platform_description()
	return render(request, 'appStore/detail.html' , {'app': app, 'platform':platform} )

     