from django.contrib import admin
from .models import (
	EdibleItem,
	Beverage,
	PackedItem,
	)

# Register your models here.
admin.site.register(EdibleItem)
admin.site.register(Beverage)
admin.site.register(PackedItem)