from rest_framework import serializers,viewsets
from .models import Funding

class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Funding
        fields='__all__'

class FundingViewSet(viewsets.ModelViewSet):
    queryset = Funding.objects.all()
    serializer_class = FundingSerializer
