from django.urls import path

from .views import SignUpView
from .views import profile, profile_view


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', profile, name='profile_detail'),
    path('profile_view/<int:pk>/', profile_view, name='profile_view'),
]