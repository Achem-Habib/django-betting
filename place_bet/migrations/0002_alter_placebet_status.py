# Generated by Django 4.0.5 on 2022-08-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place_bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placebet',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('won', 'Won'), ('lost', 'Lost'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
    ]