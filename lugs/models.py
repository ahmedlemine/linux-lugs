from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Lug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    # logo = models.ImageField()
    # todo make it a list
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # location on mape
    # occurrence
    contact_person = models.CharField(max_length=200)
    # todo: make a list
    contact_info = models.TextField()
    donate_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
