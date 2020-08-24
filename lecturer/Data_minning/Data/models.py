from django.db import models
from django.contrib.auth.models import User 
import random
from django.utils import timezone


class Nurse(models.Model):
    username = models.CharField(max_length=255,null=True)     
    firstname=models.CharField(max_length=255,null=True,blank=True)
    lastname=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField()
    password =models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.username
    


class Patient(models.Model):
    firstname=models.CharField(max_length=255,null=True,blank=True)
    lastname=models.CharField(max_length=255,null=True,blank=True)
    Next_of_kin=models.CharField(max_length=255,null=True,blank=True)
    card =models.CharField(max_length=255,null=True,blank=True)
    date_admitted = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(max_length=255)
    possible_diagnosis =models.CharField(max_length=255)



    def __str__(self):
        return self.firstname

  

class AssignPatient(models.Model):
    date_added =models.DateTimeField(auto_now_add=True)
    ward = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE,null=True)
    nurse = models.ForeignKey(Nurse, related_name='nurse',on_delete=models.CASCADE,null=True)
    Discharge = models.IntegerField(default=0)
    Death = models.IntegerField(default=0)
    date_discharged= models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.patient.firstname


