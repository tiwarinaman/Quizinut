from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Student(models.Model):
    uname = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_image = models.ImageField(upload_to='student_profile/', null=True)

    def __str__(self):
        return f"{self.uname.first_name} {self.uname.last_name}"


class Teacher(models.Model):
    uname = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_image = models.ImageField(upload_to='teacher_profile/', null=True)

    def __str__(self):
        return f"{self.uname.first_name} {self.uname.last_name}"


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    quiz_name = models.CharField(max_length=200, null=True)
    total_question = models.IntegerField(null=True)
    added_question = models.IntegerField(null=True)
    total_marks = models.IntegerField(null=True)
    time_duration = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quiz_name} By - {self.teacher.uname.first_name} {self.teacher.uname.last_name}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    question = models.TextField(blank=True, null=True)
    marks = models.PositiveIntegerField(null=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question} - {self.quiz.quiz_name}"