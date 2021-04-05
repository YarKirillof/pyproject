from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ImageField

from .models import Profile


#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
class SignUpForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ('username',
                  )
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fio',
                  'bio',
                  'location',
                  'birth_date',
                  'height',
                  'size',
                  'shoe',
                  'phone',
                  'pass_data',)

