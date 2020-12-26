from django.db import models

from teacher.models import Teacher

class Subject(models.Model):
    title = models.CharField(max_length=100)
    dtcreate = models.DateTimeField(auto_now_add=True)
    dtupdate = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
