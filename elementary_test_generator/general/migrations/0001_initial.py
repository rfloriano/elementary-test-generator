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
                ('answers', models.ManyToManyField(to='general.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_template', models.CharField(max_length=500, verbose_name='Question template')),
                ('answer_template', models.CharField(max_length=500, verbose_name='Answer template')),
                ('answer_quantity', models.PositiveIntegerField(verbose_name='Answer quantity')),
                ('question_property', models.CharField(max_length=500, verbose_name='Question property')),
                ('answer_property', models.CharField(max_length=300, verbose_name='Answer property')),
                ('query', models.TextField(null=True, verbose_name='Sparql query', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='template',
            field=models.ForeignKey(to='general.Template'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ManyToManyField(to='general.Question'),
        ),
    ]
