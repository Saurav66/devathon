from django.db import models

# Create your models here.

from django.db import models

from django.urls import reverse
from datetime import datetime
# Create your models here.


class Token(models.Model):
    reg_id = models.CharField(max_length=6)
    item_name = models.CharField(max_length=30)
  #  item_cost = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('vendor:order')


class ExtraItems(models.Model):
    item_name = models.CharField(max_length=100, primary_key=True)
    item_cost = models.CharField(max_length=10)
