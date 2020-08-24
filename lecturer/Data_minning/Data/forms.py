from django import forms
from . models import Nurse,Patient,AssignPatient
import random
from django.contrib.auth.models import User





class DoctorForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = [
        "username","first_name","last_name","email","password"
        ]

        widgets = {

            'password':forms.PasswordInput(attrs={'style':'color:black;','class':'form-control','require':'required','placeholder':'password'}),
            'username':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'username'}),
            'first_name':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'firstname'}),
            'last_name':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'lastname'}),
            'email':forms.EmailInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'email'}),
        }
    
        def save(self, commit=True):
            user = super().save(commit=False)
            username = self.cleaned_data['username']
            firstname = self.cleaned_data['first_name']
            lastname  = self.cleaned_data['last_name']
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if commit:
                user.save()

            return user


# class NurseProfileForm(forms.ModelForm):
#     class Meta: 
#         model = User
#         fields = [
#         "username","first_name","last_name","email","password"
#         ]

#         widgets = {

#             'password':forms.PasswordInput(attrs={'style':'color:black;','class':'form-control','require':'required','placeholder':'password'}),
#             'username':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'username'}),
#             'first_name':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'firstname'}),
#             'last_name':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'lastname'}),
#             'email':forms.EmailInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'email'}),
#         }
    

# class AddNurseProfileForm(forms.ModelForm):
#     class Meta:
#         model = NurseProfile

#         fields = ('number',)
#         def save(self, commit=True):
#             user = super().save(commit=False)
#             username = self.cleaned_data['username']
#             firstname = self.cleaned_data['firstname']
#             lastname  = self.cleaned_data['lastname']
#             email = self.cleaned_data['email']
#             password = self.cleaned_data['password']

#             if commit:
#                 user.save()

#             return user


class NurseForm(forms.ModelForm):
    # password=forms.CharField(widget=passwordInput())
    class Meta:
        model = Nurse
        fields = ["username","firstname","lastname","email","password"]
        widgets = {

            'password':forms.PasswordInput(attrs={'style':'color:black;','class':'form-control','require':'required','placeholder':'password'}),
            'username':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'username'}),
            'firstname':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'firstname'}),
            'lastname':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'lastname'}),
            'email':forms.EmailInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'email'}),
        }
    
        def save(self, commit=True):
            user = super().save(commit=False)
            username = self.cleaned_data['username']
            firstname = self.cleaned_data['firstname']
            lastname  = self.cleaned_data['lastname']
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if commit:
                user.save()

            return user
            



class PatientForm(forms.ModelForm):
    # password=forms.CharField(widget=passwordInput())
    class Meta:

        # def card():
        #     letter = ('A','B','C','D','E','F','G','H','I','J')
        #     for i in range(1):
        #         x = list[str(random.randint(1,1000)) + random.choice(letter)]
        #         return(x)
                
        model = Patient
        letter = ('A','B','C','D','E','F','G','H','I','J')
        fields = ["firstname","lastname","Next_of_kin","card","possible_diagnosis","symptoms"]
        widgets = {

            'card':forms.TextInput(attrs={'style':'color:black;','value':str(random.randint(1,1000))+random.choice(letter),'class':'form-control','require':'required','readonly':'readonly','placeholder':'card'}),
            'Next_of_kin':forms.TextInput(attrs={'style':'color:black;','class':'form-control','require':'required','placeholder':'Kin'}),
            'possible_diagnosis':forms.Textarea(attrs={'style':'color:black;font-size: 20px;resize:none;height:100%;max-height:100px;','row':5,'column':10,'class':'form-control','require':'required','placeholder':'please input diagnosis'}),
            'firstname':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'firstname'}),
            'lastname':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'lastname'}),            
            'symptoms':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required','placeholder':'symptoms'}),
        
        }
        

        
        # print(x)
    

        def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
            return user



class AssignPatientForm(forms.ModelForm):
    # password=forms.CharField(widget=passwordInput())
    class Meta:
        model = AssignPatient
        fields = ["nurse","patient","ward"]
        widgets = {
         
        #  'nurse':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required'}),
        #  'patient':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required'}),            
        #  'ward':forms.TextInput(attrs={'style':'color:black;font-size: 20px;','class':'form-control','require':'required'}),
        
            
        }
    
        def save(self, commit=True):
            user = super().save(commit=False)

            if commit:
                user.save()

            return user
