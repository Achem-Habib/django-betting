# Generated by Django 4.0.5 on 2022-09-12 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_article_delete_publication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-date_joined']},
        ),
    ]