# Generated by Django 4.2.1 on 2023-09-01 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_subtasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtasks',
            old_name='subtask',
            new_name='task',
        ),
    ]
