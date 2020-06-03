
from django.conf.urls import url
from django.contrib import admin
from accounts.views import login_view
from .views import *
appname="accounts"
urlpatterns = [
      url(r'^$',login_view),
      url(r'accounts/login',login_view),
    url(r'accounts/logout/',logout_view),   
     url('register/',register_view),
]
