from rest_framework import viewsets
from .models import Student, Teacher, Course, Exam , CodeSnapshot
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer, ExamSerializer , CodeSnapshotSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class CodeSnapshotViewSet(viewsets.ModelViewSet):
    queryset = CodeSnapshot.objects.all()
    serializer_class = CodeSnapshotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)