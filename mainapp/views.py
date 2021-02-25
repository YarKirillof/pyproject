from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# from orders.forms import OrderForm
from .forms import CastingForm

from .models import Casting


class MainappListView(ListView):
    model = Casting
    template_name = 'home.html'


class MainappDetailView(DetailView):
    # form = OrderForm()
    model = Casting
    template_name = 'casting_detail.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = CastingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполненена неверно'

    form = CastingForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)


# def profile(request):
#
#     return render(request, 'create.html', data)





