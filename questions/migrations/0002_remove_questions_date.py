# Generated by Django 4.1.5 on 2023-02-24 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='date',
        ),
    ]
