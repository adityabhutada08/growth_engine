from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lead
from .serializers import LeadSerializer
from automation.tasks import process_new_lead


class LeadCreateAPIView(APIView):

    def get_client_ip(self, request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:

            ip = x_forwarded_for.split(',')[0]

        else:

            ip = request.META.get('REMOTE_ADDR')

        return ip


    def get_user_agent(self, request):

        return request.META.get('HTTP_USER_AGENT')


    def check_duplicate(self, phone, email):

        return Lead.objects.filter(
            phone=phone,
            email=email
        ).exists()


    def post(self, request):

        data = request.data.copy()

        # Get tracking info
        ip_address = self.get_client_ip(request)

        user_agent = self.get_user_agent(request)

        # Check duplicate
        is_duplicate = self.check_duplicate(
            phone=data.get('phone'),
            email=data.get('email')
        )

        # Add tracking fields
        data['ip_address'] = ip_address

        data['user_agent'] = user_agent

        data['is_duplicate'] = is_duplicate

        serializer = LeadSerializer(data=data)

        if serializer.is_valid():
            # Trigger async processing
            lead = serializer.save()
            process_new_lead.delay(str(lead.id))

            return Response(
                {
                    "success": True,
                    "lead_id": str(lead.id),
                    "is_duplicate": is_duplicate
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Trigger async processing
