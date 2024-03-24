from django.urls import path

from . import views
from .views import UserLoginView, UserLogoutView, ProfileView, signup, profile

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('update_avg_caffeine_intake/', views.update_avg_caffeine_intake, name='update_avg_caffeine_intake'),
]

# forms.py

# urls.py
