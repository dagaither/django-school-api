# Generated by Django 5.0.3 on 2024-03-23 00:22

import django.core.validators
import grade_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_app', '0002_alter_grade_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0), grade_app.validators.validate_grade]),
        ),
    ]
