# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Pharmacy
from django.views.decorators.cache import cache_control
from django.contrib import messages
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def home(request):
	data=Pharmacy.objects.all()
	return render(request,"home.html",{'data':data})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add(request):
	if request.method=="POST":
		n=request.POST['mname']
		c=request.POST['mcom']
		d=request.POST['mdesc']
		s=request.POST['mtotal']
		p=request.POST['mprice']
		if(n!='' and c!='' and d!='' and s!='' and p!=''):
			med=Pharmacy.objects.filter(MedName=n)
			if med.exists():
				messages.error(request,"medicine already exists use edit opition")
				return redirect("/dashboard/add")
			else:
				med=Pharmacy(MedName=n,MedComp=c,MedDesc=d,MedTotal=s,Med1Cost=p)
				med.save()
				messages.info(request,"Inserted data successfully")
				return redirect("/dashboard/add")
		messages.info(request,"Some Empty field are there check once")		
		return redirect("/dashboard/add")
	return render(request,"add.html",{})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit(request):
	data=Pharmacy.objects.all()
	return render(request,"edit.html",{'data':data})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def update(request, id):
    d = Pharmacy.objects.get(id=id)
    if request.method=="POST":
		n=request.POST['mname']
		c=request.POST['mcom']
		des=request.POST['mdesc']
		s=request.POST['mtotal']
		p=request.POST['mprice']
		if(n!="" and c!="" and des!="" and s!="" and p!=""):
			d.MedName=n
			d.MedComp=c
			d.MedDesc=des
			d.MedTotal=s	
			d.Med1Cost=p
			d.save()
			messages.info(request,"Inserted data ")
			return redirect("/dashboard/edit")
		messages.error(request,"Some fields are empty ")
    
    return render(request,"update.html",{'data':d})

def tablet(request):
	if request.is_ajax and request.method == "GET":
		tab = request.GET.get("tablet", None)
		d=Pharmacy.objects.get(MedName=tab)
        	if Pharmacy.objects.filter(MedName = tab).exists() and d.MedTotal>0:
			
			r=list(Pharmacy.objects.filter(MedName=tab).values())
			data=dict()
			data['r']=r
			d.MedTotal=d.MedTotal-1
			d.save()
			return JsonResponse(data)
	
def delete(request, id):
	d=Pharmacy.objects.get(id=id)
	d.delete()
	messages.info(request,"Deleted datat")
	return redirect("/dashboard/edit")
