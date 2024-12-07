from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def user_login(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = User.objects.filter(username=username).first()
      if user is not None and user.check_password(password):
         request.session['user_id'] = user.id
         return redirect('dash:dashboard')
      else:
         messages.error(request, 'Invalid username or password')
         return redirect('auth:login')
   return render(request, 'auth/login.html')

def signup(request):
   if request.method == "POST":
      username = request.POST.get('username')
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email = request.POST.get('email')
      password = request.POST.get('pass1')
      confirm_password = request.POST.get('pass2')

      if password == confirm_password:
         if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('auth:signup')
         else:
            if User.objects.filter(email=email).exists():
               messages.error(request, 'Email already exists')
               return redirect('auth:signup')
            else:
               user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
               user.save()
               return redirect('auth:login')
      else:
         messages.error(request, 'Passwords do not match')
         return redirect('auth:signup')
   return render(request, 'auth/signup.html') 

def user_logout(request):
   if 'user_id' in request.session:
      del request.session['user_id']
   return redirect('auth:login')
