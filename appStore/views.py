from django.http import HttpResponse
from django.template import loader
from .models import App


def index(request):
	all_apps = App.objects.all()
	template = loader.get_template('appStore/index.html')
	context = {
		'all_apps': all_apps,
	}
	return HttpResponse(template.render(context, request))

def detail(request, app_id):
	return HttpResponse('<h2>Details for app ' + str(app_id) + '</h2>')

   