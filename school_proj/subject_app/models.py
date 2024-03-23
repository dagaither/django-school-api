from django.db import models

# Create your models here.
from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_subject_name, validate_professor_name


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=50, unique=True, validators=[validate_subject_name])
    professor = models.CharField(max_length=50, validators=[validate_professor_name])

    def __str__(self):
        students_count = self.students.count()
        return f"{self.subject_name} - {self.professor} - {students_count}"
    
    def add_a_student(self, id):
        if self.students.count() >= 30:
            raise ValidationError("This subject is full!")
        self.students.add(id)

    def drop_a_student(self, id):
        if self.students.count() == 0:
            raise ValidationError("This subject is empty!")
        self.students.remove(id)