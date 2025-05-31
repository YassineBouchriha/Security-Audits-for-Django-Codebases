from django.db import models
from django.contrib.auth import get_user_model

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Exam for {self.course.title} on {self.date}"

class CodeSnapshot(models.Model):
    file = models.FileField(upload_to='code_snapshots/')
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
# Placeholder for other models
# class Department(models.Model): ...
# class Assignment(models.Model): ...