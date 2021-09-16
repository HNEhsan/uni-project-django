from django.db import models
from secretary.models import Term, Lesson
from student.models import EducationBackground
# Create your models here.



class TeacherRegister(models.Model):
    NationalCode = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Tele = models.CharField(max_length=8)
    Phone = models.CharField(max_length=11)
    Address = models.CharField(max_length=250)



class TeacherInfo(models.Model):
    TeacherId = models.CharField(max_length=20, primary_key=True)
    NationalCode = models.ForeignKey(TeacherRegister, on_delete=models.CASCADE)
    Degree = models.CharField(max_length=100)
    TermContractNumber = models.IntegerField(default=1)


class Request(models.Model):
    ReqId = models.CharField(max_length=20, primary_key=True)
    TeacherId = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE)
    Lesson = models.CharField(max_length=50)
    TermDate = models.DateTimeField('Term Date you want presentiantion')
    Description = models.CharField(max_length=200)


class SalaryReports(models.Model):
    TransactionId = models.CharField(max_length=100, primary_key=True)
    NationalCode = models.ForeignKey(TeacherRegister, on_delete=models.CASCADE)
    #TermId
    TermId = models.ForeignKey(Term, on_delete=models.CASCADE)
    Price = models.CharField(max_length=10)
    Date = models.DateTimeField('Deposit Date')
    Status = models.CharField(max_length=100)


class StudentScore(models.Model):
    ScoreId = models.CharField(max_length=20, primary_key=True)
    TeacheId = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE)
    #StudentId
    StudentId = models.ForeignKey(EducationBackground, on_delete=models.CASCADE)
    #LessonId
    LessonId = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    Score = models.IntegerField(default=0)
    VerifyDegree = models.BooleanField()

