from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ProfileEditForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile(request, pk):
    queryset = Profile.objects.prefetch_related('user').filter(user__id=pk).first()
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


#class ProfileListView(generic.ListView):
#    success_url = reverse_lazy('profile')
#    template_name = 'profile.html'
#   def get_queryset(self):
#        self.profile = Profile.objects.prefetch_related('user').filter(user__exact=User.objects.get(pk=self.kwargs.get('pk')))



# def ProfileListView(request):




