from django import template
register = template.Library()

@register.filter
def level(queryset, category):
    return queryset.get(category)
