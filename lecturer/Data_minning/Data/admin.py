from django.contrib import admin
from . models import Nurse,Patient,AssignPatient
# Register your models here.


# @admin.register(Administrator)
# class AdministratorAdmin(admin.ModelAdmin):
#     '''Admin View for '''

#     list_display = ('user','firstname','lastname','email')
  

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('id','username','firstname','lastname','email','password')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('firstname','lastname','Next_of_kin','card','date_admitted','possible_diagnosis','symptoms')




@admin.register(AssignPatient)
class AssignPatientAdmin(admin.ModelAdmin):
    '''Admin View for AssignPatient'''

    list_display = ('id','nurse','nurse_id','patient_id','patient','ward','date_added','Discharge','Death','date_discharged')




  