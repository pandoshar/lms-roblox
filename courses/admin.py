from django.contrib import admin

# Register your models here.
from .models import Choice, Course, CourseModule, Lesson, Question, Quiz

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

class QuestionInline(admin.TabularInline):
    model=Question
    extra=1
    fields=['order','text']
    show_change_link=True

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3
    fields=['text','is_correct']
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display=['title','module','pass_score']
    inlines =[QuestionInline]
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['text','quiz','order']
    list_filter=['quiz']
    inlines=[ChoiceInline]