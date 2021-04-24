from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views.generic import ListView
from xhtml2pdf import pisa

from my_project import settings
from orders.forms import OrderForm, OrderCreationForm
from orders.models import Order
from .forms import CastingForm
from .models import Casting


class MainappListView(ListView):
    model = Casting
    template_name = 'home.html'


def index(request):
    castings = Casting.objects.select_related('author').all().order_by('-created')
    casting_male = Casting.objects.filter(category='Мужчина')
    casting_female = Casting.objects.filter(category='Женщина')
    casting_children = Casting.objects.filter(category='Ребенок')
    error = ''
    order = Order.objects.filter(user_id=request.user.id)
    cast_ids = []
    for cast in order:
        cast_ids.append(cast.casting.id)
    if request.method == 'POST':
        if request.user.fio is not None and request.user.location is not None and request.user.birth_date is not None and request.user.height is not None and request.user.size is not None and request.user.shoe is not None and request.user.phone is not None and request.user.pass_data is not None and request.user.photo is not None:
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
        else: error = 'Прежде чем подать заявку заполните профиль!'
    form = OrderCreationForm()
    return render(request, 'home.html',
                  context={'castings': castings,'casting_male': casting_male,'casting_female':casting_female, 'form': form, 'orders': order, 'error': error, 'cast_ids': cast_ids})


def casting_detail(request, pk):
    error = ''
    casting = Casting.objects.filter(id=pk).select_related('author').first()
    orders = Order.objects.filter(user_id=request.user.id)
    cast_ids = []
    for cast in orders:
        cast_ids.append(cast.casting.id)
    orders_true = Order.objects.prefetch_related('user').filter(casting_id=pk).filter(hired=True)
    true_count = orders_true.count()
    orders_false = Order.objects.prefetch_related('user').filter(casting_id=pk).filter(hired=False)
    total_count = orders_false.count() + true_count
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
                  context={'casting': casting, 'orders_true': orders_true, 'order_false': orders_false, 'error': error,
                           'form': form, 'cast_ids': cast_ids, 'true_count': true_count, 'total_count': total_count})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CastingForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.image = form.data.get('image')
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


def edit_casting(request, pk):
    if request.method == 'POST':
        form = CastingForm(request.POST, request.FILES, instance=Casting.objects.filter(id=pk).first())
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CastingForm(instance=Casting.objects.filter(id=pk).first())
    return render(request, 'edit_casting.html', context={'form': form})

def convert_html_to_pdf(request, pk):
    orders_true = Order.objects.prefetch_related('user').filter(casting_id=pk).filter(hired=True)
    template_path = 'pdf1.html'
    context = {'orders': orders_true, 'media': settings.MEDIA_ROOT}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def view_orders(request):
    orders_f = Order.objects.filter(user_id=request.user.id)
    cast_ids = []
    for cast in orders_f:
        cast_ids.append(cast.casting.id)
    return render(request, 'orders_view.html', context={'orders': orders_f,'cast_ids':cast_ids})
