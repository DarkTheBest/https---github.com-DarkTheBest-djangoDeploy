# Generated by Django 4.1.5 on 2023-02-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
