from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def date_difference(value, arg):
    try:
        due_date = datetime.strptime(arg, '%Y-%m-%d').date()
        days_difference = (due_date - value).days
        return days_difference
    except:
        return None
