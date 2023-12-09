from django.db import models


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return str(self.full_name)


class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Course Categories"

    def __str__(self):
        return str(self.title)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    address = models.TextField()
    interested_categories = models.ManyToManyField(
        CourseCategory, blank=True, related_name="interested_students"
    )

    def __str__(self):
        return str(self.full_name)
