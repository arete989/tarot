# Generated by Django 3.1.7 on 2023-11-03 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231102_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReadingCross',
            new_name='CrossReading',
        ),
        migrations.RenameModel(
            old_name='ReadingSingle',
            new_name='SingleReading',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
