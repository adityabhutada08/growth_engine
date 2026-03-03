from django.shortcuts import render
from leads.models import Lead
from django.db.models import Count, Sum
from django.db.models import Q
from django.shortcuts import redirect


def update_status(request, lead_id, new_status):

    lead = Lead.objects.get(id=lead_id)
    lead.status = new_status
    lead.save()

    return redirect('dashboard-leads')


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

    sales_leaderboard = Lead.objects.filter(
        status='converted').values(
        'assigned_to__name').annotate(
        total_revenue=Sum('revenue')).order_by('-total_revenue')

    context = {
        "total_leads": total_leads,
        "converted": converted,
        "conversion_rate": conversion_rate,
        "leads_by_campaign": leads_by_campaign,
        "sales_leaderboard": sales_leaderboard,
    }

    return render(request, "dashboard/dashboard.html", context)


def dashboard_leads(request):

    query = request.GET.get('search')
    status_filter = request.GET.get('status')

    leads = Lead.objects.all().order_by('-created_at')

    if query:
        leads = leads.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )

    if status_filter:
        leads = leads.filter(status=status_filter)

    context = {
        "leads": leads,
        "status_choices": Lead.STATUS_CHOICES
    }

    return render(request, "dashboard/leads.html", context)