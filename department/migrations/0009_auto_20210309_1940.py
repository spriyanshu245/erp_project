# Generated by Django 3.1.2 on 2021-03-09 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0008_auto_20210309_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extracurr2',
            old_name='name_of_department',
            new_name='department',
        ),
    ]
