# Generated by Django 3.2.2 on 2022-02-26 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nni', models.PositiveIntegerField(unique=True)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255, null=True)),
                ('adresse', models.CharField(max_length=255, null=True)),
                ('tel', models.CharField(max_length=255, null=True)),
                ('qrCode', models.ImageField(blank=True, null=True, upload_to='client/qrcodes/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
