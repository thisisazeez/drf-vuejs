# Generated by Django 3.2.6 on 2021-10-30 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogger',
            old_name='description',
            new_name='body',
        ),
    ]
