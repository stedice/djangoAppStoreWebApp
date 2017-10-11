from django.conf.urls import url
from . import views


app_name = 'appStore'
 
urlpatterns = [
	# /appStore
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /appStore/{id}/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /appStore/app/add/
    url(r'^app/add/$', views.AppCreate.as_view(), name='app-add'),

    # /appStore/app/{id}/
    url(r'^app/(?P<pk>[0-9]+)/$', views.AppUpdate.as_view(), name='app-update'),

    # /appStore/app/{id}/delete
    url(r'^app/(?P<pk>[0-9]+)/delete/$', views.AppDelete.as_view(), name='app-delete'),

]
