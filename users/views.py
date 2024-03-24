from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile
from .forms import UserSignupForm, UserProfileForm, UpdateAvgCaffeineIntakeForm
from django.contrib.auth import login
from django.db import transaction


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


def profile(request):
    # Retrieve user profile and pass it to the template
    profile = request.user.profile
    context = {'user': request.user, 'profile': profile}
    return render(request, 'profile.html', context)

def update_avg_caffeine_intake(request):
    if request.method == 'POST':
        form = UpdateAvgCaffeineIntakeForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateAvgCaffeineIntakeForm(instance=request.user.profile)
    return render(request, 'update_avg_caffeine_intake.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            # from GPT-4 for handling data integrity
            with transaction.atomic():
                # Try to get the profile if it exists, or create a new one
                profile, created = Profile.objects.get_or_create(user=user)
                # Update the profile with the form data
                profile.weight = profile_form.cleaned_data.get('weight')
                profile.avg_caffeine_intake = profile_form.cleaned_data.get('avg_caffeine_intake')
                profile.duration_number = profile_form.cleaned_data.get('duration_number')
                profile.duration_type = profile_form.cleaned_data.get('duration_type')
                profile.save()
        
            login(request, user)
            return redirect('profile')
    else:
        form = UserSignupForm()
        profile_form = UserProfileForm()
    return render(request, 'users/signup.html', {'form': form, 'profile_form': profile_form})
