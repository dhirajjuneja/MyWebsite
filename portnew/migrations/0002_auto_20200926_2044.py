# Generated by Django 3.1.1 on 2020-09-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portnew', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywork',
            name='live_preview',
        ),
        migrations.AddField(
            model_name='mywork',
            name='file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
