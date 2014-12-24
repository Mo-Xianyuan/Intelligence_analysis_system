from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from WebPage import views

urlpatterns = patterns('',
    url(r'^Track/create/$',  views.create), 
)
