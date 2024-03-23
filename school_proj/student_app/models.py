from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_name, validate_email, validate_locker_combo
from subject_app.models import Subject


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, validators = [validate_name])
    student_email = models.EmailField(max_length=100, null=True, unique=True, validators = [validate_email])
    personal_email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='12-12-12', validators= [validate_locker_combo])
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField(Subject, related_name="students")



    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num):
        self.locker_number = num
        self.save()

    def student_status(self, param: bool):
        self.good_student = param
        self.save()

    def add_subject(self, id):
        if self.subjects.count() < 8:
            self.subjects.add(id)
        else:
            raise Exception('This students class schedule is full!')
        
    def remove_subject(self, id):
        if self.subjects.count() > 0:
            self.subjects.remove(id)
        else:
            raise Exception('This students class schedule is empty!')
        