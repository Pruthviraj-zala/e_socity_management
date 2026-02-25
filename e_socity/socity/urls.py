from django.urls import path
from . import views

urlpatterns = [
    path("admin/",views.adminDashboardView,name="admin_dashboard"),
    path("resident/",views.residentDashboardView,name="resident_dashboard"),
    path("guard/",views.guardDashboardView,name="guard_dashboard")
]