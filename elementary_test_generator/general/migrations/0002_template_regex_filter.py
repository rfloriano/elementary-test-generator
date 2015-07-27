# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='regex_filter',
            field=models.CharField(max_length=200, null=True, verbose_name='Exclude regex', blank=True),
        ),
    ]
