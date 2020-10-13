# Generated by Django 3.1 on 2020-09-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portnew', '0017_auto_20200927_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filestorage',
            options={'verbose_name_plural': 'File Stored'},
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
