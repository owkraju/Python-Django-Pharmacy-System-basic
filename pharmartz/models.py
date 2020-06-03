# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Pharmacy(models.Model):
	MedName=models.CharField(max_length=200)
	MedComp=models.CharField(max_length=200)
	MedDesc=models.TextField()
	MedTotal=models.IntegerField()
	Med1Cost=models.IntegerField()
	
