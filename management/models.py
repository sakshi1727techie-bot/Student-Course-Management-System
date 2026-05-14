from django.db import models


class Course(models.Model):

    course_id = models.AutoField(primary_key=True)

    course_name = models.CharField(
        max_length=100,
        unique=True
    )

    duration = models.IntegerField()

    fees = models.FloatField()

    start_date = models.DateField()

    is_active = models.BooleanField(default=True)

    description = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.course_name


class Student(models.Model):

    student_id = models.AutoField(primary_key=True)

    student_name = models.CharField(max_length=100)

    age = models.IntegerField()

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=10,
        unique=True
    )

    admission_date = models.DateField(
        auto_now_add=True
    )

    is_verified = models.BooleanField(default=False)

    address = models.TextField()

    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name
