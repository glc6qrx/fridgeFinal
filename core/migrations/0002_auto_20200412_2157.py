# Generated by Django 3.0 on 2020-04-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='exp_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
