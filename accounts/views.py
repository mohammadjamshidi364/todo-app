import email
from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

from .forms import RegisterForm
from .models import User


def registerPage(request):
    form = RegisterForm()
    # get the page the user came from
    destination = request.POST.get('next')
    
    # return authenticated user to main page
    if request.user.is_authenticated:
        return redirect('todo_items')
    
    context = {}
    
    if request.method == 'POST' :
        # get data from POST request 
        form = RegisterForm(request.POST)
        
        # check the validation of data
        if form.is_valid():
            user = form.save()
            # login user
            login(request , user)
            return redirect(destination)
        else:
            context = {'register_form':form}
        
    else:
        
        context = {'register_form':form}
            
    return render(request , 'accounts/register.html' , context)

def loginPage(request):
    

    if request.user.is_authenticated:
        return redirect('todo_items')
    
    if request.method == 'POST':
        
        next = request.POST.get('next')
        # get email/username and password to login user
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # get user with input email
            user = User.objects.get(email=email)
        except :
            # get user with input username
            user = User.objects.get(username=email)
            if user is None:
                messages.error(request , 'User does not exist')
        try:
            # get user with input username for authenticating
            email_user = User.objects.get(username=email)
            # authenticating user with username
            user = authenticate(request , email=email_user.email , password=password)
        except:
            # authentication user with email
            user = authenticate(request , email=email , password=password)
            
        if user is not None:
            login(request , user)
            return redirect(next)
        else:
            messages.error(request , 'email or password is wrong')

    
    
    context = {}
    return render(request , 'accounts/login.html' , context )

def logoutPage(request):
    
    logout(request)
    return redirect('todo_items')