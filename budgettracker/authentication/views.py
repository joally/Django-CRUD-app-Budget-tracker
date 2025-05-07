
from main_app.forms import CreateRecordForm
from django.shortcuts import render, redirect
from main_app.forms import CreateUserForm, LoginForm, UpdateRecordForm
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from main_app.models import Record

from django.contrib import messages

# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my_login")

    context = {'form':form}

    return render(request, 'authentication/register.html', context=context)


# - Login a user

def my_login(request):

    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

   

    return render(request, 'authentication/my_login.html', {'form':form})





# - Dashboard

@login_required(login_url='my_login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'dashboard.html', context=context)


# - Create a record 

@login_required(login_url='my_login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'create-record.html', context=context)




@login_required(login_url='my_login')
def update_record(request, pk):
    record=Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":

        form = UpdateRecordForm(request.POST,instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'update-record.html', context=context)


@login_required(login_url='my_login')
def singular_record(request, pk):
    
    all_records=Record.objects.get(id=pk)
    
    context = {'record': all_records}
    
    return render(request,'main_app/view-record.html', context=context)




@login_required(login_url='my_login')
def delete_record(request, pk):

    record=Record.objects.get(id=pk)
    
    record.delete()
    
    return redirect('dashboard')

# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my_login")
