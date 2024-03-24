from django.shortcuts import render

# Create your views here.
# tracker/views.py

from django.shortcuts import render
from django.http import HttpResponse

from users.models import Profile
from django.shortcuts import render, redirect

def reduce_intake_view(request):
    # Assuming the user is authenticated and their profile exists
    user_profile = Profile.objects.get(user=request.user)
    avg_caffeine_intake = user_profile.avg_caffeine_intake

    context = {
        'avg_caffeine_intake': avg_caffeine_intake,
    }
    return render(request, 'tracker/reduce_intake.html', context)


def track_caffeine_view(request):
    # Your view logic here
    return render(request, 'tracker/track_caffeine.html')

