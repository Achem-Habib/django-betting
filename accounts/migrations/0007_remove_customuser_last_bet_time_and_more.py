# Generated by Django 4.0.5 on 2022-09-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_last_bet_date_customuser_last_bet_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_bet_time',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_bet_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
