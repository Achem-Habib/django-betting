# Generated by Django 4.0.5 on 2022-09-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place_bet', '0007_alter_placebet_options_remove_placebet_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placebet',
            name='match_date',
        ),
        migrations.RemoveField(
            model_name='placebet',
            name='match_time',
        ),
        migrations.AddField(
            model_name='placebet',
            name='match_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
