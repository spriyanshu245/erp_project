# Generated by Django 3.0 on 2020-10-13 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeptProEvent3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('activity_name', models.CharField(max_length=150)),
                ('resourse_person_name', models.CharField(max_length=150)),
                ('resourse_person_contact', models.IntegerField()),
                ('no_of_participants', models.IntegerField()),
                ('event_from_date', models.DateField(default=datetime.date.today, verbose_name='From')),
                ('event_to_date', models.DateField(default=datetime.date.today, verbose_name='To')),
            ],
        ),
        migrations.CreateModel(
            name='DeptStudPart5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('student_name', models.CharField(max_length=150)),
                ('event_type', models.CharField(max_length=150)),
                ('event_name', models.CharField(max_length=150)),
                ('org_inst', models.CharField(max_length=264)),
                ('from_date', models.DateField(default=datetime.date.today, verbose_name='From')),
                ('to_date', models.DateField(default=datetime.date.today, verbose_name='To')),
                ('no_of_part', models.IntegerField(verbose_name='No of Participants')),
                ('level', models.CharField(max_length=150)),
                ('awards', models.CharField(max_length=264, verbose_name='Recognition Awards')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Electronics and Telecommunication', 'Electronics and Telecommunication'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil')], default='Computer Science', max_length=150)),
                ('Class', models.CharField(choices=[('', 'Choose...'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], default='', max_length=150)),
                ('exam_type', models.CharField(choices=[('', 'Choose...'), ('MID SEM', 'MID SEM'), ('PRELIMS', 'PRELIMS'), ('END SEM', 'END SEM')], default='', max_length=150)),
                ('subject', models.CharField(choices=[('', 'Choose...'), ((('DBMS', 'DBMS'), ('TOC', 'TOC'), ('CN', 'CN'), ('SEMP', 'SEMP'), ('ISEE', 'ISEE')), (('DBMS', 'DBMS'), ('TOC', 'TOC'), ('CN', 'CN'), ('SEMP', 'SEMP'), ('ISEE', 'ISEE'))), ((('ENTC1', 'ENTC1'), ('ENTC2', 'ENTC2'), ('ENTC3', 'ENTC3'), ('ENTC4', 'ENTC4'), ('ENTC5', 'ENTC5')), (('ENTC1', 'ENTC1'), ('ENTC2', 'ENTC2'), ('ENTC3', 'ENTC3'), ('ENTC4', 'ENTC4'), ('ENTC5', 'ENTC5'))), ((('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1')), (('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1'), ('MECH1', 'MECH1'))), ((('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5')), (('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5')))], default='', max_length=150)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('appeared', models.IntegerField()),
                ('passed', models.IntegerField()),
                ('perct', models.IntegerField(default=0)),
            ],
        ),
    ]
