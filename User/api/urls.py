from django.conf.urls import include, url
from .views import UserProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'' , UserProfileViewSet)



urlpatterns = [
	url(r'^' , include(router.urls) ),
]