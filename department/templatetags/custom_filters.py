from django import template

register = template.Library()

@register.filter
def replace_to_space(value):
    value = value.replace("_or","/")
    value = value.replace("open_","(")
    value = value.replace("_close",")")
    value = value.replace("_"," ")
    value = value.capitalize()
    value = value.replace("gfm","GFM")
    value = value.replace("hod","HOD")
    return value
