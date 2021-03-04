from .models import Casting
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


