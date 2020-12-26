from django.db import models

from student.models import Student
from subject.models import Subject


class Mark(models.Model):
    value = models.PositiveSmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    dtcreate = models.DateTimeField(auto_now_add=True)
    dtupdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.value}'
