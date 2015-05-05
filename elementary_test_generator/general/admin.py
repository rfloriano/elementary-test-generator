from django.contrib import admin

from general import models, actions


class QuestionAdmin(admin.ModelAdmin):
    actions = [actions.make_test]
    list_display = ['question', 'admin_sequence_answers']
    filter_horizontal = ['answers']
    list_filter = ['template', 'answers']


class AnswerAdmin(admin.ModelAdmin):
    filter_horizontal = ['questions']
    search_fields = ['questions__question']

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Template)
admin.site.register(models.Answer, AnswerAdmin)
