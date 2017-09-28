from django.conf.urls import url
from .views import UserProfileRegisteration
	


urlpatterns = [
	url(r'^registeration/' , UserProfileRegisteration, name = 'UserProfileRegisteration'),
]