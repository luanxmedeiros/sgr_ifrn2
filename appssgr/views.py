from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appssgr.forms import *
from django.forms import modelform_factory
from django.forms import formset_factory
from django.http.request import QueryDict
from django.contrib import messages
from appssgr.models import *
# Create your views here..

@login_required(login_url='login')
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def curso(request):
    return render(request,'curso.html')

def req_list(request):
    return ""

def req_new(request):
    return ""

def req_update(request):
    return ""

def req_delete(request):
    return ""
