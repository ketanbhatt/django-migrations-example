# Generated by Django 3.0.4 on 2020-03-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_teacher_num_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='schools',
            field=models.ManyToManyField(to='school.School'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_teachers', to='school.School'),
        ),
    ]
