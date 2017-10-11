from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import App


def IndexView(request):
	context = {'all_apps': App.objects.all()}
	return render(request, 'appStore/index.html' , context )

def DetailView(request, app_id):
	app = get_object_or_404(App, pk = app_id)
	platform = app.platform_description()
	return render(request, 'appStore/detail.html' , {'app': app, 'platform':platform} )

class AppCreate(CreateView):
	model = App
	fields = ['name','description','platform'] 

# class AppUpdate(UpdateView):
# 	model = App
# 	fields = ['name','description','platform'] 
# 	template_name_suffix = '_update_form'

# class AppDelete(DeleteView):
# 	model = App
# 	success_url = reverse_lazy('app-list')
