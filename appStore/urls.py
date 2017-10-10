from django.conf.urls import url
from . import views

urlpatterns = [
	# /appStore
    url(r'^$', views.index, name='index'),

    # /appStore/{id}/
    url(r'^(?P<app_id>[0-9]+)/$', views.detail, name='detail')
]
