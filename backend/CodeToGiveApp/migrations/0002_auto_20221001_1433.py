# Generated by Django 3.2.15 on 2022-10-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeToGiveApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairLamp',
            fields=[
                ('UserHash', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('CorrectIndices', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('ChairLampResult', models.CharField(blank=True, default=None, max_length=750, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='ChairLampResult',
        ),
    ]
