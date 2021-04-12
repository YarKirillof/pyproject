from django.urls import path

from orders.views import order_creation, order_delete
from . import views
from .views import casting_detail, index


urlpatterns = [
    path('casting/<int:pk>/', casting_detail, name='casting_detail'),
    path('casting/create_order/<int:pk>', order_creation, name='create_order'),
    path('casting/delete_order/<int:pk>', order_delete, name='delete_order'),
    path('', index, name='home'),
    path('create', views.create, name='create'),

]