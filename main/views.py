from django.shortcuts import render
from django.views.generic import detail
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .serializers import TeacherSerializer
from .models import Teacher
from rest_framework.response import Response


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    # Teacher detail by primary key
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
