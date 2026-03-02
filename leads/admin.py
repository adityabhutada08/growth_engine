from django.contrib import admin
from .models import Lead, SalesPerson

@admin.register(SalesPerson)
class SalesPersonAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'email',
        'assigned_count',
        'is_active',
        'created_at'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'email'
    )


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'email',
        'source',
        'campaign',
        'is_duplicate',
        'status',
        'created_at'
    )

    list_filter = (
        'source',
        'campaign',
        'status',
        'is_duplicate'
    )

    search_fields = (
        'name',
        'phone',
        'email'
    )