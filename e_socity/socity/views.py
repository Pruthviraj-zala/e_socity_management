from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login") #check in core.urls.py login name should exist..
def adminDashboardView(request):
    return render(request,"socity/admin_dashboard.html")

@login_required(login_url="login")
def residentDashboardView(request):
    return render(request,"socity/resident_dashboard.html")

@login_required(login_url="login")
def guardDashboardView(request):
    return render(request,"socity/guard_dashboard.html")