# Generated by Django 4.0.5 on 2022-09-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_betquestion_finished_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betquestion',
            name='identifier',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
