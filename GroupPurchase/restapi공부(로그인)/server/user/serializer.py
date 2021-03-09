from rest_framework import serializers,viewsets
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','user_id','name','isAccepted','created_at')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
