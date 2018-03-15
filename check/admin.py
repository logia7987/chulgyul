from django.contrib import admin
from .models import Event,StudyClass,Student

# Register your models here.
admin.site.register(Event)
admin.site.register(Student)
admin.site.register(StudyClass)
