from django.db import models
from secretary.models import Term
# Create your models here.


class StudentRegister(models.Model):
    NationalCode = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=50)
    FamilyName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Tele = models.CharField(max_length=8)
    Phone = models.CharField(max_length=11)
    Address = models.CharField(max_length=250)


class PaymentOfTuition(models.Model):
    TransactionId = models.CharField(max_length=100, primary_key=True)
    NationalCode = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    TermId = models.ForeignKey(Term, on_delete=models.CASCADE)
    Price = models.CharField(max_length=10)
    Date = models.DateTimeField('Deposit Date')
    Status = models.CharField(max_length=100)


class EducationBackground(models.Model):
    StudentId = models.IntegerField()
    Nationalcode = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    TransactionId = models.ForeignKey(PaymentOfTuition, on_delete=models.CASCADE) 
