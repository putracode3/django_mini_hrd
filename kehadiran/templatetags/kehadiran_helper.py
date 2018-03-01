from django import template

# import os

register = template.Library()

ROW_PER_PAGE = 5

@register.filter
def get_table_number(value, args):
    return value + ( (args - 1) * ROW_PER_PAGE )

@register.filter
def get_filename(value):
    return value.name.split('upload/')[1]
    # return os.path.basename(value.path)