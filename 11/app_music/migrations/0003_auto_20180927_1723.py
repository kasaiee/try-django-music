# Generated by Django 2.1.1 on 2018-09-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_music', '0002_auto_20180927_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='fname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='lname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nick_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
