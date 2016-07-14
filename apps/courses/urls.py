# Inside apps/appname/urls.py might look like this:
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process_course$', views.process_course), 
    url(r'^remove/(?P<course>\d)$', views.remove_course)
]