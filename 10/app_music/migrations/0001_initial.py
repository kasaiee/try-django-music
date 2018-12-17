# Generated by Django 2.1.1 on 2018-09-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('summary', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('cover', models.ImageField(null=True, upload_to='albums/%Y-%m-%d/')),
                ('rate', models.FloatField(default=0, null=True)),
                ('like', models.PositiveSmallIntegerField(default=0, null=True)),
                ('release_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('nick_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('music', models.FileField(upload_to='albums/%Y-%m-%d/')),
            ],
        ),
    ]
