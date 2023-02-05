from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authUser.views import ProfileView

router = DefaultRouter()
router.register(r'profile', ProfileView, basename='profile')
urlpatterns = router.urls


urlpatterns.extend( [
  
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.jwt')),
   
])
