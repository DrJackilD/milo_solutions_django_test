from dateutil.relativedelta import relativedelta
from django import template
from django.utils.timezone import now

register = template.Library()


@register.simple_tag
def eligible(date_of_birth):
    if date_of_birth > now().date() - relativedelta(years=13):
        return 'blocked'
    else:
        return 'allowed'


@register.simple_tag
def bizz_fuzz(random_int):
    bizz_fuzz_tag = ''
    if random_int % 3 == 0:
        bizz_fuzz_tag = 'Bizz'
    if random_int % 5 == 0:
        bizz_fuzz_tag += 'Fuzz'
    if not bizz_fuzz_tag:
        bizz_fuzz_tag = random_int

    return bizz_fuzz_tag
