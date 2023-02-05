from rest_framework.viewsets import ModelViewSet
from authUser.models import User
from authUser.serializers import ProfileSirialers



class ProfileView(ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = ProfileSirialers
    http_method_names =  ['get', 'put']
  