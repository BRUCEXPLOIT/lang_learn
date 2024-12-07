from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def sign_log(request):
    if request.method == 'POST':
        # Check if it's login or signup based on the form's data
        action = request.POST.get('action')  # Assuming you have an action field
        username = request.POST.get('username')
        password = request.POST.get('password')
        if action == 'login':  # Login Logic
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('eng_path')  # Redirect to the learning path after login
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('welcome')
        elif action == 'signup':  # Signup Logic
            email = request.POST.get('email')  # Assuming you collect an email
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('sign_log')

            else:
                messages.error(request, 'Username already exists.')
                return redirect('welcome')

    return render(request,'signup_login.html')