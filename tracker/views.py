from django.shortcuts import render
from django.http import HttpResponse
from users.models import Profile
from datetime import datetime, timedelta

def reduce_intake_view(request):
    # Assuming the user is authenticated and their profile exists
    user_profile = Profile.objects.get(user=request.user)
    avg_caffeine_intake = user_profile.avg_caffeine_intake

    context = {
        'avg_caffeine_intake': avg_caffeine_intake,
    }
    return render(request, 'tracker/reduce_intake.html', context)

def track_caffeine_view(request):
    # Retrieve the user's average caffeine intake
    user_profile = Profile.objects.get(user=request.user)
    avg_caffeine_intake = user_profile.avg_caffeine_intake

    # Retrieve dose decrease value from query parameters
    dose_decrease = int(request.GET.get('dose_decrease', 0))

    # Prepare the schedule data
    schedule = []

    # Calculate the recommended caffeine intake for each day
    caffeine_intake = avg_caffeine_intake
    current_date = datetime.now().date()

    # Calculate the number of days based on the dose decrease value
    num_days = int(avg_caffeine_intake / dose_decrease) + 1

    # Generate schedule entries
    for day in range(1, num_days + 1):
        schedule_entry = {
            'day_number': day,
            'date': current_date.strftime("%Y-%m-%d"),
            'recommended_caffeine': caffeine_intake
        }
        schedule.append(schedule_entry)

        # Update the caffeine intake for the next day based on dose decrease
        caffeine_intake -= dose_decrease

        # Ensure caffeine intake doesn't go negative
        caffeine_intake = max(caffeine_intake, 0)

        # Increment the current date for the next day
        current_date += timedelta(days=1)

    # Pass the necessary data to the template
    context = {
        'avg_caffeine_intake': avg_caffeine_intake,
        'schedule': schedule,
    }

    return render(request, 'tracker/track_caffeine.html', context)
