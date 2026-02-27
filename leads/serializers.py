from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead

        fields = '__all__'

        read_only_fields = [
            'id',
            'status',
            'ip_address',
            'user_agent',
            'is_duplicate',
            'created_at',
            'updated_at'
        ]


    def validate_phone(self, value):

        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits"
            )

        return value