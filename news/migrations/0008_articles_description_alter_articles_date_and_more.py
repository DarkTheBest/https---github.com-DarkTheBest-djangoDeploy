# Generated by Django 4.1.5 on 2023-02-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_articles_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='description',
            field=models.TextField(max_length=150, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]