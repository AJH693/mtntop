from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hit(models.Model):
	ip_address = models.CharField(max_length=15)
	count = models.IntegerField(default=0)