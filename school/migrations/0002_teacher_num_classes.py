# Generated by Django 3.0.4 on 2020-03-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='num_classes',
            field=models.IntegerField(default=0),
        ),
    ]
