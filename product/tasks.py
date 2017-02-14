# -*- coding: utf-8 -*-

import random
import decimal
from inventory.celery import app
from .models import Product

@app.task(ignore_result=True)
def change_prices():
    for product in Product.objects.all():
    	product.unit_price = decimal.Decimal(str(random.randint(800,999)) + '.99')
    	product.save()
