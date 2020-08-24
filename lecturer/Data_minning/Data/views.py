from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import NurseForm,PatientForm,AssignPatientForm,DoctorForm
from .models import Nurse,Patient,AssignPatient
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone



def index(request):

    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


@login_required
def dashboard(request):

    return render(request,'Doctors/dashboard.html')


@login_required
def Nurse_dashboard(request):
    nurse = request.session.get("nurse_id")
    dd=''
    dd = Nurse.objects.get(id=nurse)
    
    nurse_name=dd.username
       
   
    return render(request,'Nurse/Nurse_dashboard.html',{'nurse_name':nurse_name})
    # return render(request,'Nurse/Nurse_dashboard.html')


@login_required
def logout(request):
    return redirect('Userlogin')


@login_required
def AddNurse(request):
    if request.method == "POST":
        form = NurseForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Doctors/ViewNurse')

    else:
        form = NurseForm()

    return render(request,'Doctors/AddNurse.html',{'form':form})
 

@login_required
def AddPatient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid:
            form.save()
            msg = ("You have successfully Added a new patient ")
            return render(request,'Doctors/dashboard.html',{'msg':msg})
            

    else:
        form =PatientForm()

    return render(request,'Doctors/AddPatient.html',{'form':form})

@login_required
def ViewNurse(request):

    AvailNurse = Nurse.objects.all()

    return render(request,'Doctors/ViewNurse.html',{'AvailNurse':AvailNurse})


@login_required
def ViewPatient(request):    
    AvailPatient = Patient.objects.all()
    return render(request,'Doctors/ViewPatient.html',{'AvailPatient':AvailPatient})

@login_required
def AssignNurse(request):
    if request.method == "POST":
        form = AssignPatientForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('ViewAssignedNurse')

    else:
        form =AssignPatientForm()

    return render(request,'Doctors/AssignNurse.html',{'form':form})



def ViewAssignedNurse(request):
    AssignedNurse = AssignPatient.objects.filter(Discharge=0,Death=0)
    return render(request,'Doctors/ViewAssignNurse.html',{'AssignedNurse':AssignedNurse})

def Userlogin(request):
    
    if request.method =="POST":
        if Nurse.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            nurse = Nurse.objects.get(username=request.POST['username'],password=request.POST['password'])
            
            if nurse is not None:
                user_id = nurse.id

                request.session['nurse_id']=user_id
                print(user_id)
                return redirect('Nurse_dashboard')

            elif nurse.username is not username or nurse.password is not password: 
                msg = forms.ValidationError(request,"invalid username or password")
                return render(request,'login.html',{'msg':msg})


        elif request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(username=username,password=password)

            if user is not None :
                login(request,user) 
                return redirect('dashboard')
            
            else:
                msg= "Invalid username or password"
                return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')

@login_required
def UpdateNurse(request,id):
    nurse = Nurse.objects.get(id=id)
    form = NurseForm(instance=nurse)
    if request.method=="POST":
        form = NurseForm(request.POST, instance=nurse)

        if form.is_valid:
            form.save()
        return redirect('ViewNurse')
    return render(request,'Doctors/AddNurse.html', {'form': form})

@login_required
def DeleteNurse(request,id):
    nurse = Nurse.objects.get(id=id)
    if request.method=="POST":
        nurse.delete()
        return redirect('ViewNurse')

    return render(request,'Doctors/DeleteNurse.html',{'item':nurse})


@login_required
def UpdatePatient(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    if request.method=="POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid:
            form.save()
        return redirect('ViewPatient')
    return render(request,'Doctors/AddPatient.html', {'form': form})

@login_required
def DeletePatient(request,id):
    patient = Patient.objects.get(id=id)
    if request.method=="POST":
        patient.delete()
        return redirect('ViewPatient')

    return render(request,'Doctors/DeletePatient.html',{'item':patient})



@login_required
def UpdateAssignNurse(request,id):
    patient = AssignPatient.objects.get(id=id)
    form = AssignPatientForm(instance=patient)
    if request.method=="POST":
        form = AssignPatientForm(request.POST, instance=patient)

        if form.is_valid:
            form.save()
        return redirect('ViewAssignedNurse')
    return render(request,'Doctors/AssignNurse.html', {'form': form})

@login_required
def DeleteAssignNurse(request,id):
    patient = AssignPatient.objects.get(id=id)
    if request.method=="POST":
        patient.delete()
        return redirect('ViewAssignedNurse')

    return render(request,'Doctors/DeleteAssignedNurse.html',{'item':patient})





def doctor_profile(request):
    doctor = request.user
    return render(request,'Doctors/Doctor_profile.html',{'doctor':doctor})


def UpdateDoctor(request,id):
    doctor = User.objects.get(id=id)
    form = DoctorForm(instance =doctor)
    if request.method=="POST":
        form = DoctorForm(request.POST,instance =doctor)

        if form.is_valid:
            form.save()
            msg = ("Acount Updated Successfully"+" "+doctor.username)
            return redirect('doctor_profile')        
    return render(request,'Doctors/Update_doctor.html', {'form': form})

@login_required
def NurseProfile(request,id):
    nurse = Nurse.objects.get(id=id)
    return render(request,'Nurse/Nurse_Profile.html',{'nurse':nurse})

@login_required
def DoctorViewDeadPatient(request):
    patient = AssignPatient.objects.filter(Death=1)
    return render(request,'Doctors/DoctorViewDeadPatient.html',{'patient':patient})


def DoctorViewDichargePatient(request):
    dis_patient = AssignPatient.objects.filter(Discharge=1)
    return render(request,'Doctors/DoctorViewDischargePatient.html',{'dis_patient':dis_patient})


def MyPatient(request):
    nurse = request.session.get('nurse_id')
    nm = ''
    nm = Nurse.objects.get(id=nurse)
    nurse_name= nm.username
   
    patient= AssignPatient.objects.filter(nurse_id=nurse,Death=0,Discharge=0)
    patient_count= patient.count()
    return render(request,'Nurse/MyPatient.html',{'patient_count':patient_count,'patient':patient,'nurse':nurse,'nurse_name':nurse_name})


def DpNurse(request,id):
    patient = AssignPatient.objects.get(id = id)
    patient_id = patient.id
    if request.method == "POST":
        AssignPatient.objects.filter(id=patient_id,Discharge=0,Death=0).update(Discharge=1,date_discharged=timezone.now())
        return redirect('MyPatient')
    return render(request,'Nurse/DpNurse.html',{'item':patient})



def DeadPNurse(request,id):
    nurse = request.session.get('nurse_id')
    nm = ''
    nm = Nurse.objects.get(id=nurse)
    nurse_name= nm.username
    patient = AssignPatient.objects.get( id = id)
    patient_id = patient.id
    if request.method == "POST":
        AssignPatient.objects.filter(id=patient_id,Discharge=0,Death=0).update(Death=1)
        return redirect('MyPatient')
    return render(request,'Nurse/DeadPNurse.html',{'item':patient,'nurse_name':nurse_name})


def MyDPatient(request):
    nurse = request.session.get('nurse_id')
    nm = ''
    nm = Nurse.objects.get(id=nurse)
    nurse_name= nm.username
   
    patient= AssignPatient.objects.filter(nurse_id=nurse,Death=1,Discharge=0)
    return render(request,'Nurse/ViewDeadPatient.html',{'patient':patient,'nurse':nurse,'nurse_name':nurse_name})


def MyDischargePatient(request):
    nurse = request.session.get('nurse_id')
    nm = ''
    nm = Nurse.objects.get(id=nurse)
    nurse_name= nm.username
   
    patient= AssignPatient.objects.filter(nurse_id=nurse,Death=0,Discharge=1)
    return render(request,'Nurse/ViewDischargedPatient.html',{'patient':patient,'nurse':nurse,'nurse_name':nurse_name})

