import re

from django.template import Template as DjangoTemplate, Context
from SPARQLWrapper import SPARQLWrapper, JSON


def create_questions(sender, instance, created, **kwargs):
    from .models import Question, Answer
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(instance.query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    variables = results['head']['vars']
    Question.objects.filter(template=instance).delete()
    regexp = re.compile(instance.regex_filter)
    for result in results['results']['bindings']:
        q_template = DjangoTemplate(instance.question_template)
        a_template = DjangoTemplate(instance.answer_template)
        context = {}
        for key in variables:
            value = regexp.sub('', result[key]['value'])
            context[key] = value
        question, _ = Question.objects.get_or_create(
            template=instance,
            question=q_template.render(Context(context))
        )
        rendered = a_template.render(Context(context))
        answer, _ = Answer.objects.get_or_create(answer=rendered)
        answer.questions.add(question)


# import django_rq
# django_rq.enqueue(func, foo, bar=baz)
