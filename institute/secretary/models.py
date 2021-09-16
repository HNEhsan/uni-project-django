from django.db import models
#from teacher.models import Teacher
# Create your models here.

class SecretaryRegister(models.Model):
    NationalCode = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Tele = models.CharField(max_length=8)
    Phone = models.CharField(max_length=11)
    Address = models.CharField(max_length=250)


class Term(models.Model):
    TermId = models.CharField(max_length=20, primary_key=True)
    StartDay = models.DateTimeField('start term day')
    EndDay = models.DateTimeField('end term day')
    DateNumberInWeek = models.IntegerField(default=1)
    Description = models.CharField(max_length=200)
    
    
class Lesson(models.Model):
    LessonId = models.CharField(max_length=20, primary_key=True)
    #TermId
    TermId = models.ForeignKey(Term, on_delete=models.CASCADE)
    #TeacherId
    #TeacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Studentnumber = models.IntegerField(default=0)
    ClassNumber = models.CharField(max_length=5)
    DateTime = models.DateTimeField('Day and Time start class')


class StudentSiteRegister(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20)


class TeacherSiteRegister(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20)


class SecretarySiteRegister(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20)



