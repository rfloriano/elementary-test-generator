from django.contrib import admin

from general import models, actions


class AnswerAdmin(admin.StackedInline):
    model = models.Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    actions = [actions.make_test]

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Template)
