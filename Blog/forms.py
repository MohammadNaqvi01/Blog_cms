from django.forms import fields
from .models import Post
from django import forms #form API
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.utils.translation import gettext,gettext_lazy as _
#auth also uses form api thats why to change pass fields 
#generated from UserCreationForm We needed to use forms

#WHILE TO CHANGE FIELDS OF USER MODEL GENERATED FIELDS 
# WE EDIT THEM INSIDE META CLASS



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password= forms.CharField(label=_("Password"),widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control','autocomplete':'current-password'}),strip=False)

    



class SignUpForm(UserCreationForm):
    #To Change Fields attr,labels etc
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
       #TO GIVE CLAsS TO INPUT FIELDS 
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
         
        }

class PostForm(ModelForm):

    class Meta:
        model=Post
        fields={'title','desc'}
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'})
        }