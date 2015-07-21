from django import template
register = template.Library()

@register.filter(name = 'addCSS')
def addCSS(field, css):
    """Add CSS class to widget"""
    return field.as_widget(attrs={"class": css})

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)