from django import template
from datetime import timedelta

register = template.Library()


@register.filter
def days_difference(value):
    now = value['now']
    my_date = value['my_date']
    difference = now - my_date
    return difference.days
