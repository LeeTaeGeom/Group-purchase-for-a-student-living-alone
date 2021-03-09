
from rest_framework import viewsets,routers
from .models import Funding
from .serializers import FundingSerializer,FundingParticipantsSerializer
from django.urls import path
class FundingViewSet(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer

class FundingParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingParticipantsSerializer

