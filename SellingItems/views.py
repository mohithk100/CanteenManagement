from django.shortcuts import render
from .models import (
	EdibleItem,
	Beverage,
	PackedItem,
	)


def EdibleItemView(request):
	EdibleItem_objects = EdibleItem.objects.all()
	context = { "EdibleItem_objects": EdibleItem_objects }
	return render(request, 'SellingItems/EdibleItems.html' , context )

def BeverageView(request):
	Beverage_objects = Beverage.objects.all()
	context = { "Beverage_objects":Beverage_objects }
	return render(request, 'SellingItems/Beverages.html' , context )

def PackedItemView(request):
	PackedItem_objects = PackedItem.objects.all()
	context = { "PackedItem_objects": PackedItem_objects }
	return render(request, 'SellingItems/PackedItems.html' , context )
