from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, CourseViewSet, ExamViewSet , CodeSnapshotViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'code-snapshots', CodeSnapshotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]