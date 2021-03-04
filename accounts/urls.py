from django.urls import path

from .views import SignUpView
from .views import  profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('profile', ProfileListView.as_view(), name='profile'),
    path('profile/<int:pk>/', profile, name='profile_detail'),
]