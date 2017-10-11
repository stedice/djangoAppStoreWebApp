from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import App


class IndexView(ListView):
	template_name = 'appStore/index.html'
	context_object_name = 'all_apps'
	paginate_by = 10

	def get_queryset(self):
		return App.objects.all().order_by('id')


class DetailView(DetailView):
	model= App
	template_name = 'appStore/detail.html'


class AppCreate(CreateView):
	model = App
	fields = ['name','description','platform'] 


class AppUpdate(UpdateView):
	model = App
	fields = ['name','description','platform'] 
	#template_name_suffix = '_update_form'


class AppDelete(DeleteView):
	model = App

	def get_success_url(self):
		return reverse_lazy('appStore:index')
		# success_url = reverse_lazy('appStore:index')
