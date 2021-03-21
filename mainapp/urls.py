from django.urls import path
from . import views
from .views import casting_detail, index


urlpatterns = [
    path('casting/<int:pk>/', casting_detail, name='casting_detail'),
    path('', index, name='home'),
    path('create', views.create, name='create'),

]