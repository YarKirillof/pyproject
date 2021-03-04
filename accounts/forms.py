from django import forms
from .models import Profile


#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
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
                  'pass_data')
