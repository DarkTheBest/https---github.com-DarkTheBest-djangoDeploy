# Generated by Django 4.1.5 on 2023-02-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
