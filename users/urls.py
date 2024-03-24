from django.urls import path
from .views import UserLoginView, UserLogoutView, ProfileView, signup

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', signup, name='signup'),
]
