from django.contrib import admin

# Register your models here.

admin.site.site_header = "Online Learning Admin"
admin.site.site_title = "Online Learning Admin Portal"

from .models import Teacher, CourseCategory, Course, Student

admin.site.register(Teacher)
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Student)
