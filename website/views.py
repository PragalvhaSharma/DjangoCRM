# Defines the logic for handling requests and returning responses. Views are functions or 
# classes that process incoming HTTP requests, interact with models if needed, and return HTTP
# responses (such as HTML pages, JSON data, etc.).

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#pass in request
def home(request):
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Debugging: Print received data
        print(f"POST data: {request.POST}")
        print(f"Username: {username}, Password: {password}")

        if username and password:
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Login the user
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                # Redirect to the home page
                return redirect('home')
            else:
                # If authentication fails, display an error message
                messages.error(request, 'There was an error logging in. Please try again.')
        else:
            messages.error(request, 'Username and password are required.')
    
    # Render the home page template
    return render(request, 'home.html')

#function for a different logout page
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully Logged out !')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')