# Generated by Django 3.1.2 on 2020-11-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20201104_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indinst9',
            name='sector',
            field=models.CharField(choices=[('Agriculture', 'Agriculture'), ('Banking', 'Banking'), ('Construction', 'Construction'), ('Consumer durables', 'Consumer durables'), ('Engineering', 'Engineering'), ('Health care', 'Health care'), ('IT', 'IT'), ('Metal and mining', 'Metal and mining'), ('Oil and Gas', 'Oil and Gas')], max_length=150),
        ),
    ]