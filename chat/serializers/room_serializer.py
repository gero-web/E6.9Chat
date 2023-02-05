from rest_framework.serializers import  ModelSerializer
from chat.models import RoomChat

class RoomSerializer(ModelSerializer):
    
    class Meta:
        model = RoomChat
        fields = '__all__'