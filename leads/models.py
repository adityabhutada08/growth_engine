from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def save(self, *args, **kwargs):

    if self.status == 'converted' and not self.conversion_date:
        self.conversion_date = timezone.now()

    super().save(*args, **kwargs)


class SalesPerson(models.Model):

    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    assigned_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lead(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Basic Info
    name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    # Marketing Source Info
    source = models.CharField(
        max_length=100,
        help_text="facebook, google, linkedin, website"
    )

    campaign = models.CharField(
        max_length=255,
        help_text="campaign name"
    )

    utm_source = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    utm_medium = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    utm_campaign = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    # Tracking Info
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    user_agent = models.TextField(
        null=True,
        blank=True
    )

    # Status
    STATUS_CHOICES = [

    ('new', 'New'),
    ('assigned', 'Assigned'),
    ('contacted', 'Contacted'),
    ('qualified', 'Qualified'),
    ('converted', 'Converted'),
    ('lost', 'Lost'),
]

    status = models.CharField(
    max_length=50,
    choices=STATUS_CHOICES,
    default='new'
)

    # Duplicate detection
    is_duplicate = models.BooleanField(
        default=False
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    assigned_to = models.ForeignKey(
        SalesPerson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )

    revenue = models.DecimalField(
        max_digits=13,
        decimal_places=2,
        null=True,
        blank=True
    )

    conversion_date = models.DateTimeField(
        null=True,
        blank=True
    )

def __str__(self):
    return f"{self.name} - {self.phone}"