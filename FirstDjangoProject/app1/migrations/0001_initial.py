# Generated by Django 2.1.2 on 2018-10-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDados',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('telefone', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]