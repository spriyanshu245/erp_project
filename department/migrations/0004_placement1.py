# Generated by Django 3.1.2 on 2021-02-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_placement2_placement3_placement4_placement5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, max_length=4, unique_for_year=True, verbose_name='year')),
                ('companies_Visited', models.PositiveIntegerField(default=1, verbose_name='Number of Companies visited for Campus Recruitment')),
                ('students_Placed', models.PositiveIntegerField(default=1, verbose_name='Number of Students Placed')),
                ('students_placed_Percentage', models.PositiveIntegerField(default=1, verbose_name='Percentage of students placed')),
                ('max_Salary', models.PositiveIntegerField(default=1, verbose_name='Maximum Salary offered (p.a.)')),
                ('min_Salary', models.PositiveIntegerField(default=1, verbose_name='Minimum Salary offered (p.a.)')),
                ('average_Salary', models.PositiveIntegerField(default=1, verbose_name='Average of salary offered (p.a.)')),
            ],
        ),
    ]