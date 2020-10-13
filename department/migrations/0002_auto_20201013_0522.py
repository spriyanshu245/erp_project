# Generated by Django 3.1.2 on 2020-10-13 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('departments', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('employer', models.CharField(max_length=150)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('package', models.IntegerField()),
                ('ref_no', models.IntegerField()),
                ('year_admission', models.IntegerField(default=0)),
                ('year_down', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]