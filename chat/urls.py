from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views import RoomView
from chat.views import list_user

router = DefaultRouter()
router.register(r'room', RoomView, basename='room')
urlpatterns = router.urls


urlpatterns = router.urls

urlpatterns.append(path("list_user",list_user, name="list_user"))