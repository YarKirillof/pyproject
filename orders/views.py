from django.shortcuts import render, redirect

# Create your views here.
from mainapp.models import Casting
from orders.forms import OrderForm, CheckedForm
from orders.models import Order


def order_creation(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            tmp_order = form.save(commit=False)
            tmp_order.casting = Casting.objects.filter(id=pk).first()
            tmp_order.user = request.user
            tmp_order.hired = True
            form.save()
            return redirect('casting_detail', pk=pk)


def order_delete(request, pk):
    if request.method == 'POST':
        Order.objects.filter(casting_id=pk).filter(user_id=request.user.id).delete()
        return redirect('home')


def checked_out(request):
    if request.method == 'POST':
        value = request.POST.get('checked_out')
        order = Order.objects.filter(id=request.POST.get('order_id')).first()
        form = CheckedForm(request.POST, instance=order)
        if form.is_valid():
            tmp_order = form.save(commit=False)
            if value == 'True':
                tmp_order.checked_out = False
            elif value == 'False':
                tmp_order.checked_out = True
            form.save()
            return redirect('casting_detail', pk=order.casting.pk)
