import re

from django.template import Template as DjangoTemplate, Context
from SPARQLWrapper import SPARQLWrapper, JSON

from .utils import make_query


def create_questions(sender, instance, created, **kwargs):
    from .models import Question, Answer
    if not instance.query:
        make_query(instance)
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(instance.query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    variables = results['head']['vars']
    Question.objects.filter(template=instance).delete()
    if instance.regex_filter:
        regexp = re.compile(instance.regex_filter)
    for result in results['results']['bindings']:
        q_template = DjangoTemplate(instance.question_template)
        a_template = DjangoTemplate(instance.answer_template)
        context = {}
        for key in variables:
            value = result[key]['value']
            if instance.regex_filter:
                value = regexp.sub('', value)
            context[key] = value
        question, _ = Question.objects.get_or_create(
            template=instance,
            question=q_template.render(Context(context))
        )
        rendered = a_template.render(Context(context))
        answer, _ = Answer.objects.get_or_create(answer=rendered)
        answer.questions.add(question)
