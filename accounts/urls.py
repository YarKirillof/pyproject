from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm
from .views import SignUpView
from .views import profile, profile_view, view_actors


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm), name='login'),
    path('profile/<int:pk>/', profile, name='profile_detail'),
    path('profile_view/<int:pk>/', profile_view, name='profile_view'),
    path('view_actors/', view_actors, name='view_actors'),
]