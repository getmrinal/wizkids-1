# Generated by Django 2.0.2 on 2018-10-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0003_auto_20181002_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='cid',
            new_name='ids',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='coursename',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='topicdesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='tid',
            new_name='ids',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='topicname',
            new_name='title',
        ),
    ]
