from django.urls import path
from .views import TeacherList

urlpatterns = [
    path('teacher/', TeacherList.as_view()),
]