from fnmatch import fnmatchcase
from lib2to3.pgen2 import token
import uuid
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import calc
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method ==  "POST":
        username= request.POST.get("user")
        password = request.POST.get("passw")
        user_obj = User.objects.filter(username=username).first()
        profile_obj = calc.objects.filter(user=user_obj).first()

        user=auth.authenticate(username=username,password=password)

        

        if user is not None :
            if profile_obj.is_varified == False:
                messages.success(request, 'Your email has not been verified please verify your email')
                return redirect('home')
            else:
                return render(request , "home.html")   
                
        else:
            messages.success(request, 'Invalid credentials try again')
            return redirect('home')
            
    else:

        return render(request,'Signin.html')

def signup(request):

    if request.method ==  "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phoneno = request.POST.get("phoneno")
        dob = request.POST.get("dob")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email=request.POST.get("email")
        rques = request.POST.get("rques")
        rans = request.POST.get("rans")

        if User.objects.filter(username=username).first() and User.objects.filter(email=email).first():
            messages.error(request, 'Username and email already exist')
            return redirect('signup')

        if User.objects.filter(username=username).first():
            messages.error(request, 'Username already exist')
            return redirect('signup')

        if User.objects.filter(email=email).first():
            messages.error(request, 'Email already in use')
            return redirect('signup')

        user = User.objects.create_user(username=username,email=email,password=password)
        user.first_name = name
        user.last_name = surname
        user.save()
        tokens=str(uuid.uuid4())
        extra = calc(user=user,mobile=phoneno,rans=rans,rques=rques,birthday=dob,token=tokens)
        extra.save()

        sendmail(email,tokens)
        return HttpResponse('verification link has been sent on your email please verify to login')


    return render(request, "signup.html")

def signout(request):
    pass

def main(request):
    return render(request, "home.html")

def sendmail(email,token):
    subject = "your account needs to be verified"
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


def verify(request, token):
    profile_obj = calc.objects.filter(token=token).first()
    if profile_obj:
        if profile_obj.is_varified == True:
            messages.success(request, 'Your email has already been verified')
            return redirect('home')
        else:
            profile_obj.is_varified = True
            profile_obj.save()
            messages.success(request, 'Your email has been verified now you can login')
            return redirect('home')
    else:
        return HttpResponse('error')
    
