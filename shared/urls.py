from django.urls import path
from . import views
from users.views import UserLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('users/login/', UserLoginView.as_view(), name='login')
]
