# Generated by Django 4.0.5 on 2022-08-01 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_publication_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
