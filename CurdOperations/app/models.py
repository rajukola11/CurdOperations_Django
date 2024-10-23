from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.IntegerField()
    address=models.CharField(max_length=250)
    skills=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
