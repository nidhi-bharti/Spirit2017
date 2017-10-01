# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def spirit(request):
    my_dict={'insert':"check templates"}
    return render(request,'home/home.html',context = my_dict)
