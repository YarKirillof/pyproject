from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import ProfileEditForm, SignUpForm, LoginForm
from .models import Profile

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
        form = ProfileEditForm(request.POST, request.FILES, instance=queryset)
        file = form.data.get('photo')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.photo = form.data.get('photo')
            post.save()
            return redirect('home')
        else:
            error = form.errors
    form = ProfileEditForm(instance=queryset)
    return render(request, 'profile.html', context={'queryset': queryset, 'form': form, 'error': error})


def profile_view(request, pk):
    query = Profile.objects.filter(id=pk).first()
    return render(request, 'profile_view.html', context={'query': query})


def view_actors(request):
    query = Profile.objects.all()
    return render(request, 'view_actors.html', context={'query': query})
