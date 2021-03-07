from django.urls import path
from . import views
from .views import MainappListView, MainappDetailView, casting_detail


urlpatterns = [
    path('casting/<int:pk>/', casting_detail, name='casting_detail'),
    path('', MainappListView.as_view(), name='home'),
    path('create', views.create, name='create'),

]