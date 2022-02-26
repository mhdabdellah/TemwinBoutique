# Generated by Django 3.2.2 on 2022-02-26 13:59

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_nni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nni',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10)]),
        ),
    ]
