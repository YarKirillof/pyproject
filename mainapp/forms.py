from .models import Casting
from accounts.models import Profile
from django.forms import ModelForm, TextInput, DateTimeField, Textarea


class CastingForm(ModelForm):
    class Meta:
        model = Casting
        author = 'auth.User'
        fields = ['title', 'category', 'height', 'size', 'sizeshoe',
                  'place', 'date', 'time', 'hour', 'description', 'fee']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            # "author": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Агентство'
            # }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            "height": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рост'
            }),
            "size": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Размер_одежды'
            }),
            "sizeshoe": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Размер_обуви'
            }),
            "place": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес_локации'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время_сбора'
            }),
            "hour": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время_занятости'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Требования'
            }),
            "fee": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ставка'
            }),
            # "": TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': ''
            # }),

        }


from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group



class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
         queryset=Profile.objects.all(),
         required=False,
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance