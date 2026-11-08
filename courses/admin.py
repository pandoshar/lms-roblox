from django.contrib import admin

# Register your models here.
from .models import Course, CourseModule, Lesson

class CourseModuleInline(admin.TabularInline):
    model = CourseModule
    extra=1
    fields = ['title', 'order']
    show_change_link = True
class LessonInline(admin.StackedInline):
    model = Lesson
    extra=1
    fields =['title','content','order']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    inlines = [CourseModuleInline]

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    ordering = ['course', 'order']
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'order']
    list_filter = ['module__course','module']
    search_fields = ['title','content']
 