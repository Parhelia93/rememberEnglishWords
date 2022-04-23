from django import template
from englishWords.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if filter == None:
        return ProgressCat.objects.all()
    else:
        return ProgressCat.objects.filter(pk=filter)


@register.inclusion_tag('englishWords/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = ProgressCat.objects.all()
    else:
        cats = ProgressCat.objects.order_by(sort)
    return {'cats':cats, 'cat_selected':cat_selected}