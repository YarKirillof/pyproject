from django.urls import path

from orders.views import order_creation, order_delete, checked_out
from . import views
from .views import casting_detail, index, convert_html_to_pdf, view_orders, edit_casting

urlpatterns = [
    path('casting/<int:pk>/', casting_detail, name='casting_detail'),
    path('casting/create_order/<int:pk>', order_creation, name='create_order'),
    path('casting/delete_order/<int:pk>', order_delete, name='delete_order'),
    path('', index, name='home'),
    path('casting/checked_out/', checked_out, name='checked_out'),
    path('create', views.create, name='create'),
    path('casting/pdf_render/<int:pk>', convert_html_to_pdf, name='pdf_creation'),
    path('orders_view/', view_orders, name='orders_view'),
    path('edit_casting/<int:pk>', edit_casting, name='edit_casting')

]