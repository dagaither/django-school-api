# Generated by Django 5.0.3 on 2024-03-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0007_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]