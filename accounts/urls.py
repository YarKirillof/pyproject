from django.urls import path

from .views import SignUpView
from .views import ProfileListView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile', ProfileListView.as_view(), name='profile'),
    # path('profile/<int:pk>/', ProfileListView.as_view(), name='profile_detail'),
]