# Generated by Django 3.1.2 on 2020-11-07 13:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0007_auto_20201107_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCurr1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=150)),
                ('organized_by', models.CharField(max_length=150)),
                ('level', models.CharField(max_length=150)),
                ('date', models.DateField(default=datetime.date.today)),
                ('number_of_students_participated', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCurr2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_sport_or_team', models.CharField(max_length=250, verbose_name='Name of the Sport / Team')),
                ('student_ID_number', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('name_of_department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]