from django.conf.urls import url
from . import views


app_name = 'appStore'
 
urlpatterns = [
	# /appStore
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /appStore/{id}/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /appStore/add/
    url(r'^add/$', views.AppCreate.as_view(), name='app-add'),

]
