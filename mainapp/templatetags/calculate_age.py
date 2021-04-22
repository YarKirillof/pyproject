from datetime import date

from django import template

register = template.Library()

@register.filter(name='calculate_age')
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))