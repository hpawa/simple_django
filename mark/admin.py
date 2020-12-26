from django.contrib import admin

from .models import Mark
from subject.models import Subject

class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ['value', 'subject']


admin.site.register(Mark, SubjectAdmin)
