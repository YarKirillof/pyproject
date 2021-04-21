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
    order = Order.objects.filter(user_id=request.user.id)
    cast_ids = []
    for cast in order:
        cast_ids.append(cast.casting.id)
    if request.method == 'POST':
        casting_id = request.POST.get('casting_id')
        order = Order.objects.filter(casting_id=casting_id, user_id=request.user.id).first()
        if order:
            error = 'Заявка уже существует'
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                tmp_order = form.save(commit=False)
                tmp_order.casting = Casting.objects.filter(id=casting_id).first()
                tmp_order.user = request.user
                tmp_order.hired = True
                form.save()
                return redirect('home')
    form = OrderCreationForm()
    return render(request, 'home.html', context={'castings': castings, 'form': form, 'orders': order, 'error': error, 'cast_ids' : cast_ids})


def casting_detail(request, pk):
    error = ''
    casting = Casting.objects.filter(id=pk).first()
    orders = Order.objects.filter(user_id=request.user.id)
    cast_ids = []
    for cast in orders:
        cast_ids.append(cast.casting.id)
    orders_true = Order.objects.prefetch_related('user').filter(casting_id=pk).filter(hired=True)
    orders_false = Order.objects.prefetch_related('user').filter(casting_id=pk).filter(hired=False)
    if request.method == 'POST':
        value = request.POST.get('test_id')
        order = Order.objects.filter(id=request.POST.get('order_id')).first()
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            tmp_order = form.save(commit=False)
            if value == 'True':
                tmp_order.hired = False
                tmp_order.checked_out = False
            elif value == 'False':
                tmp_order.hired = True
            form.save()
            return redirect('casting_detail', pk=casting.id)
        else:
            error = form.errors
    form = OrderForm()
    return render(request, 'casting_detail.html',
                  context={'casting': casting, 'orders_true': orders_true, 'order_false': orders_false, 'error': error, 'form': form, 'cast_ids':cast_ids})


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


