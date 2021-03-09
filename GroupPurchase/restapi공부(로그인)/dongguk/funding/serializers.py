from rest_framework import serializers
from .models import Funding

class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Funding
        fields=('title','description','price','except_destionation','additional','categories')

class FundingParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Funding
        fields=('participants.User.username','participants.User.id')

