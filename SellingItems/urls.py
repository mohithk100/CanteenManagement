from django.conf.urls import url
from .views import (
	EdibleItemView,
	BeverageView,
	PackedItemView,
	)


urlpatterns = [
	url(r'^edibles/' , EdibleItemView , name = 'EdibleItemView' ),
	url(r'^beverages/' , BeverageView , name = 'BeverageView' ),
	url(r'^packeditems/' , PackedItemView, name = 'PackedItemView' ),
]