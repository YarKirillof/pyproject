from django.urls import path
from . import views
from .views import MainappListView, MainappDetailView


urlpatterns = [
    path('casting/<int:pk>/', MainappDetailView.as_view(), name='casting_detail'),
    path('', MainappListView.as_view(), name='home'),
    path('create', views.create, name='create'),

]