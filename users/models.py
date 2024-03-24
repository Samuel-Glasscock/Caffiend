from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(default=0.0)
    avg_caffeine_intake = models.IntegerField(default=0)
    # duration_number = models.IntegerField(default=0)
    # duration_type = models.CharField(max_length=5, choices=(('days', 'Days'), ('weeks', 'Weeks')), default='days')

