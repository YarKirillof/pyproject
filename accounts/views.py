from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ProfileEditForm, SignUpForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile(request, pk):
    queryset = Profile.objects.filter(id=pk).first()
    error = ''
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=queryset)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
        else:
            error = form.errors
    form = ProfileEditForm(instance=queryset)
    return render(request, 'profile.html', context={'queryset': queryset, 'form': form, 'error': error})




