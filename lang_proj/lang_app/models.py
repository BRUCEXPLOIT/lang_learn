from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse

def authenticate_user(request):
    if request.method == "POST":
        action = request.POST.get('action')  # Identify if it's login or signup
        role = request.POST.get('role')  # Role from the form (student/tutor)

        if action == "signup":
            # Signup logic
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Create the user in the specified role database
            with connections[role].cursor():
                User.objects.db_manager(role).create_user(username=username, email=email, password=password)
            return HttpResponse(f"User {username} signed up successfully in {role} database!")

        elif action == "login":
            # Login logic
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Authenticate user in the specified role database
            user = authenticate(request, username=email, password=password, role=role)

            if user:
                login(request, user)  # Django handles session creation
                return HttpResponse(f"Welcome {user.username}! You are logged in as {role}.")
            else:
                return HttpResponse("Invalid credentials. Please try again.")
    return render(request, "signup_login.html")  # Render the combined form page
