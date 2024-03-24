
# tracker/urls.py

from django.urls import path
from . import views
from .views import track_caffeine_view

app_name = 'tracker'  # Set the app_name attribute

urlpatterns = [
    path('reduce-intake/', views.reduce_intake_view, name='reduce_intake'),
    # Other URL patterns for the 'tracker' app
    path('reduce-intake/track_caffeine/', views.track_caffeine_view, name='track_caffeine'),  # Updated URL pattern
]
