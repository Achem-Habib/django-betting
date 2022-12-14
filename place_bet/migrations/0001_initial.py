# Generated by Django 4.0.5 on 2022-08-02 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('match_category', models.CharField(max_length=100)),
                ('tournament_name', models.CharField(blank=True, max_length=200, null=True)),
                ('match_date', models.DateField(blank=True, null=True)),
                ('match_time', models.TimeField(blank=True, null=True)),
                ('team_1', models.CharField(max_length=100)),
                ('team_2', models.CharField(max_length=100)),
                ('question_id', models.IntegerField()),
                ('question', models.CharField(max_length=250)),
                ('answer_id', models.IntegerField()),
                ('answer', models.CharField(max_length=250)),
                ('rate', models.FloatField()),
                ('amount', models.FloatField(default=0)),
                ('return_amount', models.FloatField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
