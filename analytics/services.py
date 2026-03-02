from leads.models import Lead
from django.db.models import Count, Sum


def total_leads():
    return Lead.objects.count()


def leads_by_campaign():
    return Lead.objects.values('campaign').annotate(
        total=Count('id')
    )


def conversion_rate():
    total = Lead.objects.count()
    converted = Lead.objects.filter(status='converted').count()

    if total == 0:
        return 0

    return (converted / total) * 100


def revenue_by_campaign():
    return Lead.objects.filter(
        status='converted'
    ).values('campaign').annotate(
        revenue=Sum('revenue')
    )


def sales_performance():
    return Lead.objects.filter(
        status='converted'
    ).values('assigned_to__name').annotate(
        conversions=Count('id'),
        revenue=Sum('revenue')
    )