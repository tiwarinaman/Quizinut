from django.contrib import admin

from .models import Student, Teacher, Quiz, Question

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Quiz)
admin.site.register(Question)
