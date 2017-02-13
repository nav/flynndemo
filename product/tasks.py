# -*- coding: utf-8 -*-

from inventory.celeryapp import app

@app.task(ignore_result=True)
def change_prices(name, **kwargs):
    