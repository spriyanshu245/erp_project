# Generated by Django 3.1.2 on 2021-03-01 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0008_auto_20210301_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library1',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='January', max_length=150, verbose_name='Month'),
        ),
    ]
