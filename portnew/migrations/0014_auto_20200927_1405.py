# Generated by Django 3.1 on 2020-09-27 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portnew', '0013_auto_20200927_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestorage',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portnew.userid'),
        ),
    ]
