from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


def make_test(modeladmin, request, queryset):
    context = dict(
        modeladmin.admin_site.each_context(request),
        queryset=queryset,
    )
    return TemplateResponse(request, 'general/make_test.html', context)
make_test.short_description = _('Generate a new test')
