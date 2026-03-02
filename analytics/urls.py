from django.urls import path
from .views import AnalyticsDashboardAPIView

urlpatterns = [
    path('dashboard/', AnalyticsDashboardAPIView.as_view()),
]