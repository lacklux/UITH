from django.urls import path,include
from Data import views  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('Userlogin',views.Userlogin,name='Userlogin'),
    path('about',views.about, name='about'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('Doctors/AddNurse',views.AddNurse,name='AddNurse'),
    path('Doctors/AddPatient',views.AddPatient,name='AddPatient'),
    path('Doctors/ViewNurse',views.ViewNurse,name='ViewNurse'),
    path('Doctors/ViewPatient',views.ViewPatient,name='ViewPatient'),
    path('Doctors/AssignNurse',views.AssignNurse,name='AssignNurse'),
    path('Doctors/UpdateNurse/<str:id>/',views.UpdateNurse,name='UpdateNurse'),
    path('Doctors/DeleteNurse/<str:id>/',views.DeleteNurse,name='DeleteNurse'),
    path('Doctors/UpdatePatient/<str:id>/',views.UpdatePatient,name='UpdatePatient'),
    path('Doctors/DeletePatient/<str:id>/',views.DeletePatient,name='DeletePatient'),
    path('Doctors/UpdateAssignNurse/<str:id>/',views.UpdateAssignNurse,name='UpdateAssignNurse'),
    path('Doctors/DeleteAssignNurse/<str:id>/',views.DeleteAssignNurse,name='DeleteAssignNurse'),
    path('Nurse/MyDPatient',views.MyDPatient,name='MyDPatient'),
    path('Nurse/MyDischargePatient',views.MyDischargePatient,name='MyDischargePatient'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('UpdateDoctor/<str:id>/',views.UpdateDoctor,name='UpdateDoctor'),
    path('Doctors/ViewAssignedNurse/',views.ViewAssignedNurse,name='ViewAssignedNurse'),
    path('Doctors/DoctorViewDeadPatient',views.DoctorViewDeadPatient,name='DoctorViewDeadPatient'),
    path('Doctors/DoctorViewDichargePatient',views.DoctorViewDichargePatient,name='DoctorViewDichargePatient'),
    path('Nurse/Nurse_dashboard',views.Nurse_dashboard,name='Nurse_dashboard'),
    path('Nurse/MyPatient',views.MyPatient,name='MyPatient'),
    path('DpNurse/<str:id>/',views.DpNurse,name="DpNurse"),
    path('DeadPNurse/<str:id>/',views.DeadPNurse,name="DeadPNurse"),

    
    
    #password reset path
    path('password_change_done',auth_views.PasswordChangeDoneView.as_view(
    template_name='registration/password_change_dones.html'),name='password_change_done'),
     
    path('password_change',auth_views.PasswordChangeView.as_view(
    template_name='registration/password_change.html'),name='password_change'),

    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(
    template_name='registration/password_reset_dones.html'),name='password_reset_done'),
     
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),
     
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name= 'registration/password_reset_forms.html'),name='password_reset'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(
    template_name='registration/password_reset_complete.html'),name='password_reset_complete')
    

]
