# Generated by Django 2.1.1 on 2018-09-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_music', '0003_auto_20180927_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
