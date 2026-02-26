from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required
# Create your views here.
#check in core.urls.py login name should exist..
@role_required(allowed_roles=['ADMIN'])
def adminDashboardView(request):
    return render(request,"socity/admin/admin_dashboard.html")

@role_required(allowed_roles=['RESIDENT'])
def residentDashboardView(request):
    return render(request,"socity/resident/resident_dashboard.html")

@role_required(allowed_roles=['GUARD'])
def guardDashboardView(request):
    return render(request,"socity/guard/guard_dashboard.html")