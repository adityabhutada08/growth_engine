from django.urls import path
from .views import dashboard_home, leads_list

urlpatterns = [
    path('', dashboard_home, name='dashboard-home'),
    path('leads/', leads_list, name='dashboard-leads'),
]