from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def date_difference(value, arg):
    print(value,"9999999999999999")
    try:
        due_date = datetime.strptime(arg, '%Y-%m-%d').date()
        days_difference = (due_date - value).days
        return days_difference
    except:
        return None
