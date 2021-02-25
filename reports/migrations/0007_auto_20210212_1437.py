# Generated by Django 3.1.2 on 2021-02-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20180427_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatereports',
            name='month',
            field=models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=2021),
        ),
        migrations.AlterField(
            model_name='generatereports',
            name='year',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)], default=2021),
        ),
    ]
