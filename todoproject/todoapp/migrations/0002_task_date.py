# Generated by Django 5.0.6 on 2024-08-18 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-10-27'),
            preserve_default=False,
        ),
    ]