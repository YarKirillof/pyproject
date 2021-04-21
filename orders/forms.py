from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('hired',)


class CheckedForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('checked_out',)

class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('casting',
                  'user',)
