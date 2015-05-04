# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=500, verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=500, verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_template', models.CharField(max_length=500, verbose_name='Question template')),
                ('answer_template', models.CharField(max_length=500, verbose_name='Answer template')),
                ('regex_filter', models.CharField(max_length=200, null=True, verbose_name='Exclude regex', blank=True)),
                ('query', models.TextField(verbose_name='Sparql query')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='template',
            field=models.ForeignKey(to='general.Template'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='general.Question'),
        ),
    ]
