from django.db import models
from django.contrib.auth.models import User
import os

class Medicines(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    price = models.CharField(max_length=20, blank=False)