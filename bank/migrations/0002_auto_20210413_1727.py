# Generated by Django 3.2 on 2021-04-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='from_account',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_account',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
