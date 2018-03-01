from django import template

register = template.Library()

ROW_PER_PAGE = 5

@register.filter
def get_table_number(value, args):
    return value + ( (args - 1) * ROW_PER_PAGE )