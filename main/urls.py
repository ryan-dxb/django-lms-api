from django.urls import path

from .views import TeacherList, TeacherDetail, CategoryList, CourseList

urlpatterns = [
    path("teacher/", TeacherList.as_view()),
    path("teacher/<int:pk>", TeacherDetail.as_view()),
    path("course-category/", CategoryList.as_view()),
    path("course/", CourseList.as_view()),
]
