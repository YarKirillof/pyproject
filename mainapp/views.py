from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from orders.forms import OrderForm, OrderCreationForm
from orders.models import Order
from .forms import CastingForm

from .models import Casting


class MainappListView(ListView):
    model = Casting
    template_name = 'home.html'


def index(request):
    castings = Casting.objects.all()
    error = ''
    order = None
    if request.method == 'POST':
        casting_id = request.POST.get('casting_id')
        order = Order.objects.filter(casting_id=casting_id, user_id=request.user.id)
        form = OrderForm(request.POST)
        if form.is_valid():
            tmp_order = form.save(commit=False)
            tmp_order.casting = Casting.objects.filter(id=casting_id).first()
            tmp_order.user = request.user
            form.save()
            return redirect('home')
        else:
            error = form.errors
    form = OrderCreationForm()
    return render(request, 'home.html', context={'castings': castings, 'form': form, 'order': order})


def casting_detail(request, pk):
    error = ''
    casting = Casting.objects.filter(id=pk).first()
    orders = Order.objects.prefetch_related('user').filter(casting_id=pk)
    if request.method == 'POST':
        value = request.POST.get('test_id')
        order = Order.objects.filter(id=request.POST.get('order_id')).first()
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            tmp_order = form.save(commit=False)
            if value == 'True':
                tmp_order.hired = False
            elif value == 'False':
                tmp_order.hired = True
            form.save()
            return redirect('casting_detail', pk=casting.id)
        else:
            error = form.errors
    form = OrderForm()
    pass
    return render(request, 'casting_detail.html',
                  context={'casting': casting, 'orders': orders, 'error': error, 'form': form})


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
