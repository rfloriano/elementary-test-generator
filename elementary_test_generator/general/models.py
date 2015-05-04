from random import shuffle

from django.db import models
from django.utils.translation import ugettext_lazy as _

from general import signals


ANSWERS_NUMBER = 5


class Template(models.Model):
    question_template = models.CharField(_('Question template'), max_length=500)
    answer_template = models.CharField(_('Answer template'), max_length=500)
    regex_filter = models.CharField(_('Exclude regex'), max_length=200, null=True, blank=True)
    query = models.TextField(_('Sparql query'))

    def __str__(self):
        return self.question_template.encode('utf-8')


class Question(models.Model):
    question = models.CharField(_('Question'), max_length=500)
    template = models.ForeignKey(Template)

    def __str__(self):
        return self.question.encode('utf-8')

    def right_answers(self):
        return Answer.objects.filter(question=self).order_by('?')

    def wrong_answers(self):
        return Answer.objects.filter(
            ~models.Q(question=self),
            question__template=self.template
        ).order_by('?')

    def get_answers(self, quantity=ANSWERS_NUMBER):
        answers = list(self.right_answers())
        answers += list(self.wrong_answers()[:quantity - 1])
        shuffle(answers)
        return answers


class Answer(models.Model):
    answer = models.CharField(_('Answer'), max_length=500)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.answer.encode('utf-8')


models.signals.post_save.connect(signals.create_questions, sender=Template)
