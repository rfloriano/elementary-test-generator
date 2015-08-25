from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from general.models import Template


class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ['question_template', 'answer_quantity', 'question_property',
                  'answer_property', 'answer_template']
        labels = {
            'question_template': _('What is question template?'),
            'answer_quantity': _('How many answers?'),
            'question_property': _('Where is {{ property }}?'),
            'answer_property': _('Which is association to {{ property }}?'),
            'answer_template': _('What is answer template?'),
        }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }


class QueryForm(ModelForm):
    class Meta:
        model = Template
        fields = ['query']
        labels = {
            'query': _('Query'),
        }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
