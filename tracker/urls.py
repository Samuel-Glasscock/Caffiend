
# tracker/urls.py

from django.urls import path
from . import views

app_name = 'tracker'  # Set the app_name attribute

urlpatterns = [
    path('reduce-intake/', views.reduce_intake_view, name='reduce_intake'),
    # Other URL patterns for the 'tracker' app
]
