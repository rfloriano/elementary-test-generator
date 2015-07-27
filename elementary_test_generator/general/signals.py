import re

from django.template import Template as DjangoTemplate, Context
from SPARQLWrapper import SPARQLWrapper, JSON

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


def create_questions(sender, instance, created, **kwargs):
    from .models import Question, Answer
    if not instance.query:
        q_match = TEMPLATE_VARS.search(instance.question_template)
        if not q_match:
            raise RuntimeError('None var found in {0}'.format(instance.question_template))

        a_match = TEMPLATE_VARS.search(instance.answer_template)
        if not a_match:
            raise RuntimeError('None var found in {0}'.format(instance.answer_template))

        template = DjangoTemplate(BASE_QUERY)
        instance.query = template.render(Context({
            'question': q_match.group(1).strip(),
            'answer': a_match.group(1).strip(),
            'question_property': instance.question_property,
            'answer_property': instance.answer_property,
        }))
        instance.save()
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
