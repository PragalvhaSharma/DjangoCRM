# Defines the logic for handling requests and returning responses. Views are functions or 
# classes that process incoming HTTP requests, interact with models if needed, and return HTTP
# responses (such as HTML pages, JSON data, etc.).

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record 

#pass in request
def home(request):
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records': records})

#function for a different logout page
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully Logged out !')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')

def register_user(request):
    #If they are filling out the form
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error registering your account.')
    else:
        #If they are just getting the form
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

#returns the recrod based on primary key
def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_record = Record.objects.get(id=pk) #getting a singel object
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'Please log in to view that page')
        
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Sucessfully!')
        return redirect('home')
    else:
        messages.success(request, 'Please log in!')
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_records.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk) #grabbing record nd passing it back to the form
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')