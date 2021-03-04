from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# from orders.forms import OrderForm
from orders.models import Order
from accounts.models import Profile
from .forms import CastingForm

from .models import Casting


class MainappListView(ListView):
    model = Casting
    template_name = 'home.html'


class MainappDetailView(DetailView):
    model = Casting
    template_name = 'casting_detail.html'

# def casting_detail(request, pk):
#     casting = Casting.objects.filter(id=pk).first()
#     profiles = Profile.objects.prefetch_related('user_id').filter(user__in=o)
#     orders = Order.objects.prefetch_related('user').filter(casting_id=pk)
#     return render(request, 'casting_detail.html', context={'casting': casting, 'orders': orders})

def create(request):
    error = ''
    if request.method == 'POST':
        form = CastingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = CastingForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)


# def profile(request):
#
#     return render(request, 'create.html', data)





