from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework.response import Response

class TeacherList(generics.ListCreateAPIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
   