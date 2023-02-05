from rest_framework.viewsets import ModelViewSet
from chat.models import RoomChat
from chat.serializers.room_serializer import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

class RoomView(ModelViewSet):
    
    queryset = RoomChat.objects.all()
    serializer_class = RoomSerializer
  
    
@api_view(['GET'])    
def list_user(req):
    lst = list(User.objects.all().values_list("id",'username'))
    
    return Response(lst)
    
