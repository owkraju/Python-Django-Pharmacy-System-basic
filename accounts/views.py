# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import UserRegisterForm,UserLoginForm
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
def login_view(request):
	
	next=request.GET.get("next")
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		login(request,user)
		if next:
			return redirect(next)
		return redirect("dashboard/")
	context={"form":form}
	return render(request,"login.html",context)
def register_view(request):
	next=request.GET.get("next")
	form=UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		newuser=authenticate(username=user.username,password=password)
		login(request,newuser)
		if next:
			return redirect(next)
		return redirect("../dashboard/")
	context={"form":form}
	return render(request,"signup.html",context)
@login_required

def logout_view(request):
	request.session.flush()
	logout(request)
	return  redirect("/")
