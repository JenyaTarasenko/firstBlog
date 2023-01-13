from django import template
from women.models import *



register = template.Library()

#пользовательский тег шаблона
@register.simple_tag()
def get_categories():
    return Category.objects.all()


#@register.inclusion_tag('women/list_catigories.html')
#def show_categories():
    #cats = Category.objects.all()
    #return {'cats': cats}
