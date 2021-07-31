from django import http
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import LoginForm, SignUpForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import Post
from django.contrib.auth.models import Group
from datetime import date
from django.contrib.auth.models import User
# Create your views here.
 
 # HOME
def home(request):
    posts=Post.objects.all()
    # user=request.user
    # print(user) output equals request.user.username
    time=60*60*24*7
    
    return render(request,'Blog/home.html',{'post':posts,'time':time})


 # ABOUT

def about(request):
    return render(request,'Blog/about.html')


# Contact

def contact(request):
    time=60*60*24*7
    return render(request,'Blog/contact.html',{'time':time})



# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
       posts=Post.objects.all()  
       user=request.user
       full_name=user.get_full_name() 
       joined=user.date_joined   
       gps=user.groups.all()
       return render(request,'Blog/dashboard.html',{'post':posts,'full_name':full_name,'groups':gps,'joined':joined})
    else:
        return HttpResponseRedirect('/login')



# Login
def user_login(request):

#REQUEST.USER IS A BUILT IN VAR WHICH TELL US ABOUT WHICH USER IS LOGGED IN RIGHT NOW
    if not request.user.is_authenticated:
     if request.method=="POST":
        lg=LoginForm(request=request,data=request.POST)
        if lg.is_valid():
            uname=lg.cleaned_data['username']
            pwd=lg.cleaned_data['password']

            user=authenticate(username=uname,password=pwd)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                #MESSGE WILL go to dashboard page through httpresponseredirecr
                return HttpResponseRedirect('/dashboard')
    
     else:
      lg=LoginForm()
      return render(request,'Blog/login.html',{'login':lg})
    return HttpResponseRedirect('/dashboard/')
# Logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
# Signup

def signup(request):

    if request.method=="POST":
      
       form=SignUpForm(request.POST)
       if form.is_valid():
        messages.success(request,"Congratulations!! you are an Author now")
        user=form.save()
        group=Group.objects.get(name="Author")
        user.groups.add(group)  
    else:   
       form=SignUpForm()
    return render(request,'Blog/signup.html',{'myform':form})


#Add New Post


def add_post(request):
   if request.user.is_authenticated:
       if request.method=='POST':
           fm=PostForm(request.POST)
           if fm.is_valid():
               joined=date.today()
               user=request.user
               
               title=fm.cleaned_data['title']
               desc=fm.cleaned_data['desc']
               pst=Post(title=title,desc=desc,date_created=joined,created_by=user)
               pst.save()#could have saved directly after populating the date but taking cleaned data if preferred
               messages.success(request,"Post Added Successfully!!")
            
               fm=PostForm()
       else:
          fm=PostForm()       
       return render(request,'Blog/addpost.html',{'form':fm})
   else:
       return HttpResponseRedirect('/login/')

#Update Post


def update_post(request,id):
   if request.user.is_authenticated:
             if request.method=='POST':
                 fm=PostForm(request.POST)
                 if fm.is_valid():
                        fm.save()
                        messages.success(request,"Post Updated Successfully!!")
             else:
                   pi=Post.objects.get(pk=id)

                   fm=PostForm(instance=pi)       
             return render(request,'Blog/updatepost.html',{'form':fm})
           
               
      
   else:
     return HttpResponseRedirect('/login/')

#Delete Post


def delete_post(request,id):
   if request.user.is_authenticated:
       if request.method=="POST":
          dlt=Post.objects.get(pk=id)
          dlt.delete()
       return HttpResponseRedirect('/dashboard')
   else:
       return HttpResponseRedirect('/login/')

