from django.db import models
import uuid


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
    status = models.CharField(
        max_length=50,
        default="new"
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

    def __str__(self):
        return f"{self.name} - {self.phone}"