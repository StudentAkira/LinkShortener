# Generated by Django 4.0.6 on 2022-07-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_shortedlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortedlink',
            name='long_url',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='shortedlink',
            name='short_url',
            field=models.URLField(default=None),
        ),
    ]
