# Generated by Django 2.0.2 on 2018-10-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0005_auto_20181004_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='cid',
            field=models.IntegerField(),
        ),
    ]
