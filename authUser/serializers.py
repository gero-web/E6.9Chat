from rest_framework.serializers import  ModelSerializer
from authUser.models import User


class ProfileSirialers(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'