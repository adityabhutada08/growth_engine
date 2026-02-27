from django.contrib import admin
from .models import Lead


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