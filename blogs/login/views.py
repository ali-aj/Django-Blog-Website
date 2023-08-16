from django.shortcuts import render, redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re
from email_validator import validate_email
import pyotp
from .models import otpClass

# Create your views here.
def redirect_view(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            logout(request)
        else:
            return redirect('/home')
    return redirect('/login')

def login_view(request):
    if request.method == 'POST':
        
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                return render(request, 'login.html', {'form': form, 'user_exist': True}) 
        else:
           return render(request, 'login.html', {'form': form, 'user_exist': True}) 
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form, 'user_exist': False}) 

def logout_view(request):
    logout(request)
    return redirect('/')

def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$"
    return re.match(pattern, password)

def register_view(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        user_exist = User.objects.filter(username=username)
        if user_exist:
            return render(request, 'register.html', {'issue': 'username'})
        password = request.POST['passwordField']    
        if not validate_password(password):
            return render(request, 'register.html', {'issue': 'password'})
        
        email = request.POST['emailField']
        valid = validate_email(email)
        if valid.email != email:
            return render(request, 'register.html', {'issue': 'email'})
        
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
        user.save()
        return redirect('/login')
    
    return render(request, 'register.html', {'issue': 'none'})

def forget_password_view(request):
    email = ''
    if request.method == 'POST':
        if request.POST['password'] == '' and request.POST['otp'] == '':
            email = request.POST['email']
            try:
                user = User.objects.get(email=email)
            except:
                email = ''
                return render(request, 'forget_password.html', {'user_exist': 'False', 'email': email})
            
            secret_key = pyotp.random_base32()
            totp = pyotp.TOTP(secret_key, digits=6)
            otp = totp.now()
            
            obj = otpClass.objects.filter(email=email).delete()
            
            otp_instance = otpClass(otp=otp, email=email)
            otp_instance.save()
            
            return render(request, 'forget_password.html', {'email': email})
        else:
            otp = request.POST['otp']
            password = request.POST['password']
            email = request.POST['email']
            if validate_password(password):
                check_otp = otpClass.objects.get(email=email)
                if check_otp.otp == otp:
                    obj = User.objects.get(email=email)
                    obj.set_password(password)
                    obj.save()
                    return redirect('/login')
                status = 'Fail'
            else:
                status = 'Password'
            return render(request, 'forget_password.html', {'email': email, 'status': status})
    return render(request, 'forget_password.html', {'email': email})
