from django.db import models

# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    password = models.CharField(max_length=32)

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=32)
    stu_sex = models.CharField(max_length=32)
    stu_major = models.ForeignKey("Major",on_delete=models.CASCADE)
    department = models.ForeignKey("Department",on_delete=models.CASCADE)
    stu_class = models.CharField(max_length=64)
    stu_phone = models.CharField(max_length=32)
    stu_address = models.CharField(max_length=32)
    stu_birthday = models.DateField()
    password = models.IntegerField(default=123456)
    isdeleted = models.IntegerField(default=0)

class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    # age = models.IntegerField()
    usersex = models.CharField(max_length=32)
    password = models.IntegerField(default=123456)
    other = models.CharField(max_length=128)
    isdeleted = models.IntegerField(default=0)
class Department(models.Model):
    # dm_id = models.IntegerField(primary_key=True)
    dm_name = models.CharField(max_length=32)
    dm_dean = models.CharField(max_length=32)
    dm_phone = models.CharField(max_length=32)
    isdeleted = models.IntegerField(default=0)

class Major(models.Model):
    # major_id = models.IntegerField(primary_key=True,)
    major_name = models.CharField(max_length=32)
    department = models.ForeignKey("Department",on_delete=models.CASCADE)
    major_teacher = models.CharField(max_length=32)
    isdeleted = models.IntegerField(default=0)

class Classes(models.Model):
    # classes_id = models.IntegerField(primary_key=True)
    classes_name = models.CharField(max_length=32)
    major = models.ForeignKey("Major",on_delete=models.CASCADE)
    classes_teacher = models.CharField(max_length=32)
    isdeleted = models.IntegerField(default=0)

