from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = patterns('',
    url(r'^index/$',  views.index), 
    url(r'^favour/(.+)/$', views.favour),
    url(r'^login/$',  views.login), 
    url(r'^register/$',  views.register),
    url(r'^register/next/$',  views.register_next),
)
