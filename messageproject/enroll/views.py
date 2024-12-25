from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def regi(request):
    fm=StudentRegistration()
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            store=User(name=nm,email=em,password=pw)
            fm=StudentRegistration()
            store.save()
            messages.add_message(request,messages.SUCCESS,"your account has beeen created!!!.")
            # return redirect('regis')
       
    else:
        fm=StudentRegistration()
    return render(request,'enroll/userregistration.html',{"form":fm})




# def hello(request):
#     return render(request,'enroll/regi.html')
        