# Generated by Django 3.2.6 on 2021-09-16 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentscore',
            name='StudentId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='student.educationbackground'),
            preserve_default=False,
        ),
    ]
