from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='modules')
    title = models.CharField(max_length=300)
    order = models. PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(fields=['course', 'order'], name='unique_order_per_course')

        ]

    def __str__(self):
        return f"{self.order}. {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=300)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(fields=['module', 'order'], name='unique_order_per_module')
        ]

    def __str__(self):
        return self.title
class Quiz(models.Model):
    module = models.OneToOneField(CourseModule, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=300)
    pass_score = models.PositiveIntegerField(
        default=70,validators=[MinValueValidator(1),MaxValueValidator(100)],

    )
    class Meta:
        verbose_name_plural='quizzes'
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text=models.TextField()
    order=models.PositiveBigIntegerField(default=1)

    class Meta:
        ordering=['order']
    def __str__(self):
        return self.text
class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices')
    text=models.CharField(max_length=300)
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.text