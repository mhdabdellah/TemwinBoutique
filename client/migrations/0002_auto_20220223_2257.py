# Generated by Django 2.2.27 on 2022-02-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nni',
            field=models.CharField(max_length=20),
        ),
    ]
