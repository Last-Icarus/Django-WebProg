from django import template

register = template.Library()

@register.filter
def date_filter(value):
    return value.replace("weeks","недель").replace("months","месяцев").replace("days","дней") \
                .replace("week","неделя").replace("month","месяц").replace("day","день")
