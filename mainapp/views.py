from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from orders.forms import OrderForm
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


def casting_detail(request, pk):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=Order.objects.filter(casting_id=pk))
        if form.is_valid():
            form.save()
            return redirect('casting_detail')
        else:
            error = form.errors
    form = OrderForm(instance=Order.objects.filter(casting_id=pk).first())
    casting = Casting.objects.filter(id=pk).first()
    orders = list(Order.objects.prefetch_related('user').filter(casting_id=pk))
    ids_list = []
    for i in orders:
        ids_list.append(i.user.id)
    profiles = Profile.objects.prefetch_related('user').filter(user_id__in=ids_list)
    return render(request, 'casting_detail.html',
                  context={'casting': casting, 'profiles': profiles, 'orders': orders, 'form': form, 'error': error})


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

