# Generated by Django 5.0.3 on 2024-03-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0009_alter_student_locker_combination_and_more'),
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='students', to='subject_app.subject'),
        ),
    ]
