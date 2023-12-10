from rest_framework import generics

from .models import Teacher, CourseCategory, Course
from .serializers import TeacherSerializer, CourseCategorySerializer, CourseSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    # Teacher detail by primary key
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
