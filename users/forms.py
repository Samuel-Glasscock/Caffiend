from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('weight', 'avg_caffeine_intake', 'duration_number', 'duration_type')


# forms.py
class UpdateAvgCaffeineIntakeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avg_caffeine_intake']

