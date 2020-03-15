from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()

class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="old_teachers", null=True)
    schools = models.ManyToManyField(School)
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=64)
