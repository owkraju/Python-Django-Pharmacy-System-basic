
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *
from . import views
appname="pharmartz"
urlpatterns = [
    url(r'^$',home),
    url(r'^home/$',home),
    url(r'^add/$',add),
    url(r'^edit/$',edit),
    url(r'^update/(?P<id>\d+)/$', update),
    url(r'^delete/(?P<id>\d+)/$', delete),
    url(r'tablet',tablet),
    
]
