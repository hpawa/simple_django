from django.db import models

from student.models import Student


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dtcreate = models.DateTimeField(auto_now_add=True)
    dtupdate = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
