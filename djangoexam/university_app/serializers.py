from rest_framework import serializers
from .models import Student, Teacher, Course, Exam , CodeSnapshot

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class CodeSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnapshot
        fields = '__all__'
        read_only_fields = ['uploaded_by', 'uploaded_at']