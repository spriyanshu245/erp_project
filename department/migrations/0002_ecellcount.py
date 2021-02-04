# Generated by Django 3.1.2 on 2021-02-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcellCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_Name', models.CharField(max_length=250)),
                ('civil', models.PositiveIntegerField(default=1)),
                ('computer', models.PositiveIntegerField(default=10)),
                ('E_andTC', models.PositiveIntegerField(default=10)),
                ('mechanical', models.PositiveIntegerField(default=10)),
                ('first_Year', models.PositiveIntegerField(default=10)),
            ],
        ),
    ]