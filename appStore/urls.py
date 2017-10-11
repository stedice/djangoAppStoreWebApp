from django.conf.urls import url
from . import views


app_name = 'appStore'
 
urlpatterns = [
	# /appStore
    url(r'^$', views.IndexView, name='index'),

    # /appStore/{id}/
    url(r'^(?P<app_id>[0-9]+)/$', views.DetailView, name='detail'),

    # /appStore/add/
    url(r'^add/$', views.AppCreate.as_view(), name='app-add'),

]
