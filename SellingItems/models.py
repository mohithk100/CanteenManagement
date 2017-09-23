from __future__ import unicode_literals
from django.db import models



class EdibleItem(models.Model):
	Name = models.CharField(max_length = 50, blank = False)
	Price = models.IntegerField(blank = False)
	Description = models.TextField(blank = True)
	Availability = models.BooleanField(default = True)
	Image = models.ImageField(upload_to = 'SellingItems/EdibleItems/' , null = True , blank = True)

	def __unicode__(self):
		return self.Name

	def __str__(self):
		return self.Name



class Beverage(models.Model):
	Name = models.CharField(max_length = 50, blank = False)
	Price = models.IntegerField(blank = False)
	Description = models.TextField(blank = True)
	Availability = models.BooleanField(default = True)
	Image = models.ImageField(upload_to = 'SellingItems/Beverages/' , null = True , blank = True)

	def __unicode__(self):
		return self.Name

	def __str__(self):
		return self.Name


class PackedItem(models.Model):
	Name = models.CharField(max_length = 50, blank = False)
	Price = models.IntegerField(blank = False)
	Description = models.TextField(blank = True)
	Availability = models.BooleanField(default = True)
	Image = models.ImageField(upload_to = 'SellingItems/PackedItems/' , null = True , blank = True)

	def __unicode__(self):
		return self.Name

	def __str__(self):
		return self.Name

