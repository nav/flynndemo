from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	sku = models.CharField(max_length=100, blank=True, default='')
	name = models.CharField(max_length=255, blank=True, default='')
	description = models.CharField(max_length=1000, blank=True, default='')
	unit_price = models.DecimalField(max_digits=16, decimal_places=2)

	
