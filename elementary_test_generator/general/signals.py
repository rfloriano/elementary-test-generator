from django.template import Template as DjangoTemplate, Context

from SPARQLWrapper import SPARQLWrapper, JSON


def create_questions(sender, instance, created, **kwargs):
    from .models import Question, Answer
    Question.objects.filter(template=instance).delete()
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(instance.query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    variables = results['head']['vars']
    for result in results['results']['bindings']:
        q_template = DjangoTemplate(instance.question_template)
        a_template = DjangoTemplate(instance.answer_template)
        context = {}
        for key in variables:
            context[key] = result[key]['value']
        question = Question.objects.create(
            template=instance,
            question=q_template.render(Context(context))
        )
        Answer.objects.create(
            question=question,
            answer=a_template.render(Context(context))
        )


# import django_rq
# django_rq.enqueue(func, foo, bar=baz)
