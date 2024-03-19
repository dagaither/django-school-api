from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    personal_email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True)
    locker_combination = models.CharField(max_length=8, default='12-12-12')
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self, num):
        self.locker_number = num
        self.save()

    def student_status(self, param: bool):
        self.good_student = param
        self.save()