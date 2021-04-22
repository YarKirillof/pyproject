from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ImageField
from django.utils.translation import gettext_lazy as _


from .models import Profile


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    _("Пожалуйста, введите корректные логин и пароль. Учтите, что логин и пароль регистрозависимы"))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("Аккаунт не активен."))
        self.check_for_test_cookie()
        return self.cleaned_data




class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', error_messages={
                                     'invalid': 'Неверный формат логина',
                                     'unique': 'Пользователь с таким именем уже существует'}
                                 )
    password1 = forms.RegexField(widget=forms.PasswordInput,
                                 regex=r'[\w+]{8,}',
                                 label='Пароль',
                                 error_messages={
                                     'invalid': 'Неверный формат пароля. Пароль должен быть не менее 8 символов, не может полностью состоять из цифр, пароль не должен быть частовстречающимся'}
                                 )
    password2 = forms.RegexField(widget=forms.PasswordInput,
                                 regex=r'[\w+]{8,}', label='Подтверждение пароля', error_messages={'invalid': 'Неверный формат пароля'})

    class Meta:
        model = Profile
        fields = ('username',
                  'password1',
                  'password2'
                  )


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(required=False)

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
                  'pass_data',
                  'photo')
