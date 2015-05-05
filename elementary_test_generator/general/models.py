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

    def __unicode__(self):
        return self.question_template


class Answer(models.Model):
    answer = models.CharField(_('Answer'), max_length=500)
    questions = models.ManyToManyField('Question')

    def __unicode__(self):
        return self.answer


class Question(models.Model):
    question = models.CharField(_('Question'), max_length=500)
    template = models.ForeignKey(Template)
    answers = models.ManyToManyField('Answer', through=Answer.questions.through)

    def __unicode__(self):
        return self.question

    def right_answers(self):
        return self.answer_set.all()

    def wrong_answers(self):
        return Answer.objects.filter(
            ~models.Q(questions=self),
            questions__template=self.template
        )

    def sequence_answers(self, answers):
        return map(lambda i: i.answer, list(answers))

    def sequence_str_answers(self, answers):
        return ', '.join(self.sequence_answers(answers))

    def admin_sequence_answers(self):
        return self.sequence_str_answers(self.right_answers())

    def get_options(self, quantity=ANSWERS_NUMBER):
        right_answers = self.right_answers().order_by('?')
        size = len(right_answers)
        answers = [self.sequence_str_answers(right_answers)]
        for i in range(quantity - 1):
            answers += [self.sequence_str_answers(
                self.wrong_answers().order_by('?')[:size])
            ]
        shuffle(answers)
        return answers

models.signals.post_save.connect(signals.create_questions, sender=Template)
