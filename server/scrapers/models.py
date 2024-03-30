from datetime import datetime
from django.db import models

from products.models import Product


class Comment(models.Model):
    text_value = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    value = models.IntegerField()
    weight = models.IntegerField()
    weighted_value = models.IntegerField()


class History(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField(default=datetime.now)
    source = models.CharField(max_length=7)
    type_scrape = models.CharField(max_length=10, default="daily")
