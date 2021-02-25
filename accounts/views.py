from django.shortcuts import render
from django.views import generic
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProfileListView(generic.ListView):
    queryset = Profile.objects.select_related('user')
    success_url = reverse_lazy('profile')
    template_name = 'profile.html'



# def ProfileListView(request):




