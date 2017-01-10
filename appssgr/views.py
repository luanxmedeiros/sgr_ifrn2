from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here..

@login_required(login_url='login')
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def curso(request):
    return render(request,'curso.html')

