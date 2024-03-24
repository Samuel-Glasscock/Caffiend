from django.db import models
from django.contrib.auth.models import User

class CaffeineIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caffeine_intake = models.IntegerField(help_text="Amount of caffeine in milligrams.")
    time_of_day = models.DateTimeField(auto_now_add=True)
    duration_of_consumption = models.IntegerField(help_text="Duration of consumption in days")
    

    def __str__(self):
        return f"{self.user}'s intake at {self.time_of_day}"


class HealthData(models.Model):
    SIDE_EFFECTS = [
        ('increased alertness', 'Increased alertness'),
        ('increased heart rate', 'Increased heart rate'),
        ('increased blood pressure', 'Increased blood pressure'),
    ]

    # WITHDRAW_SYMPTOMS = [
    #     (),
    # ]

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    heart_rate = models.IntegerField(help_text="Heart rate in beats per minute.")
    sleep_hours = models.FloatField(help_text="Average hours of sleep per night.")
    side_effects = models.CharField(max_length=100, choices=SIDE_EFFECTS)


    def __str__(self):
        return f"{self.user}'s health data"

