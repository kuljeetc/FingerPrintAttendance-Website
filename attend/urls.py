from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<inuser>S[0-9]+)/$', views.userattendance, name='userattendance'),
    url(r'^adduser$', views.adduser, name='adduser'),    
    url(r'^addattendance$', views.addattendance, name='addattendance'),
]