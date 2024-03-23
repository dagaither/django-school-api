from django.db import models
from django.core import validators as v
from .validators import validate_grade
from student_app.models import Student
from subject_app.models import Subject

# Create your models here.


class Grade(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2, validators=[v.MaxValueValidator(100.00), v.MinValueValidator(0.00), validate_grade])
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True,)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True)

    