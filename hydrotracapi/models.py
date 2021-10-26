from django.db import models
import random
import string

class Log(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    beverage = models.CharField(max_length=75)
