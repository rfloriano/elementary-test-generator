import re

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from general.forms import TemplateForm, QueryForm
from general.models import Template, Question
from general.utils import make_query


TEMPLATE_VARS = re.compile(r'{{(.*)}}')


BASE_QUERY = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX cat: <http://dbpedia.org/resource/Category:>
PREFIX dbpedia-type: <http://dbpedia.org/class/yago/>
PREFIX dbpedia-prop: <http://dbpedia.org/property/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?{{ question }} ?{{ answer }}
WHERE  {
    ?p1 a {{ question_property|safe }};
    rdfs:label ?{{ question }};
        {{ answer_property|safe }} ?p2 .
        ?p2 rdfs:label ?{{ answer }} .
    FILTER (
        langMatches(lang(?{{ question }}), "PT") &&
        langMatches(lang(?{{ answer }}), "PT")
    )
}
"""


def wizard(request):
    form = TemplateForm(request.POST)
    if form.is_valid():
        make_query(form.instance)
        form.save()
        return HttpResponseRedirect(form.instance.get_absolute_url())
    return render(request, 'general/wizard.html', {
        'formset': form
    })


def template(request, id):
    template = Template.objects.get(id=id)
    form = QueryForm(instance=template)
    if request.method == 'POST':
        form = QueryForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('general.views.questions', args=[str(template.id)]))
    return render(request, 'general/template.html', {
        'formset': form
    })


def questions(request, template_id):
    template = Template.objects.get(id=template_id)
    questions = Question.objects.filter(template=template)
    return render(request, 'general/questions.html', {
        'questions': questions
    })
