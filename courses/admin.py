from django.contrib import admin

# Register your models here.
from .models import Course, CourseModule, Lesson
admin.site.register(Course)
admin.site.register(CourseModule)
admin.site.register(Lesson)