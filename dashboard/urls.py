from django.urls import path
from .views import dashboard_home, leads_list, dashboard_leads, update_status

urlpatterns = [
    path('', dashboard_home, name='dashboard-home'),
    path('leads/', leads_list, name='dashboard-leads'),
    path('dashboard/leads/', dashboard_leads, name='dashboard-leads'),
    path('update-status/<uuid:lead_id>/<str:new_status>/', update_status, name='update-status'),
]