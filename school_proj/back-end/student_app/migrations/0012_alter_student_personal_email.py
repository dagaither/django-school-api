# Generated by Django 5.0.3 on 2024-03-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0011_alter_student_personal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]