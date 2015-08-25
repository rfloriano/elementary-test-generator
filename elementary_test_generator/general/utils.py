import re
from django.template import Template as DjangoTemplate, Context


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


def make_query(instance):
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
