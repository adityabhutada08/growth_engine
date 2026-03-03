from django.shortcuts import render
from leads.models import Lead
from django.db.models import Count


def leads_list(request):
    leads = Lead.objects.all().order_by('-created_at') # Newest first
    return render(request, "dashboard/leads.html", {"leads": leads})


def dashboard_home(request):

    total_leads = Lead.objects.count()

    converted = Lead.objects.filter(status='converted').count()

    conversion_rate = 0
    if total_leads > 0:
        conversion_rate = round((converted / total_leads) * 100, 2)

    leads_by_campaign = Lead.objects.values('campaign').annotate(
        total=Count('id')
    )

    context = {
        "total_leads": total_leads,
        "converted": converted,
        "conversion_rate": conversion_rate,
        "leads_by_campaign": leads_by_campaign,
    }

    return render(request, "dashboard/dashboard.html", context)