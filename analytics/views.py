from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    total_leads,
    leads_by_campaign,
    conversion_rate,
    revenue_by_campaign,
    sales_performance
)


class AnalyticsDashboardAPIView(APIView):

    def get(self, request):

        data = {

            "total_leads": total_leads(),

            "conversion_rate": conversion_rate(),

            "leads_by_campaign": list(leads_by_campaign()),

            "revenue_by_campaign": list(revenue_by_campaign()),

            "sales_performance": list(sales_performance())
        }

        return Response(data)