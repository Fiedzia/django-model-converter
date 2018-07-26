from django import template

register = template.Library()


@register.filter
def name4rust(name: str) -> str:
    return name.replace('.', '_')
