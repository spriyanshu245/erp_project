from django import template

register = template.Library()

@register.filter
def replace_to_space(value):
    value = value.replace("_"," ")
    return value.capitalize()
