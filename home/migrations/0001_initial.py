# Generated by Django 4.0.5 on 2022-08-12 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=False)),
                ('show', models.BooleanField(default=True)),
                ('finish_date_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatchCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_status', models.CharField(choices=[('Live', 'Live Match'), ('Upcoming', 'Upcoming Match')], default='Upcoming', max_length=50)),
                ('tournament_name', models.CharField(blank=True, max_length=100, null=True)),
                ('team_1', models.CharField(max_length=100)),
                ('team_2', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('score', models.CharField(blank=True, max_length=400)),
                ('show', models.BooleanField(default=True)),
                ('match_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_category', to='home.matchcategory')),
            ],
        ),
        migrations.CreateModel(
            name='BetRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_answer', models.CharField(max_length=250)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('win', models.BooleanField(default=False)),
                ('bet_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_rates', to='home.betquestion')),
            ],
        ),
        migrations.AddField(
            model_name='betquestion',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bet_questions', to='home.match'),
        ),
    ]
