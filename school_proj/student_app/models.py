from django.db import models
from django.core import validators as v
from .validators import validate_name, validate_email, validate_locker_combo

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, validators = [validate_name])
    student_email = models.EmailField(max_length=100, null=True, blank=True, unique=True, validators = [validate_email])
    personal_email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='00-00-00', validators= [validate_locker_combo])
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num):
        self.locker_number = num
        self.save()

    def student_status(self, param: bool):
        self.good_student = param
        self.save()