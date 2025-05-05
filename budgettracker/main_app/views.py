from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Category,Expense
from .models import Expense
from .forms import ExpenseForm

# Define the home view function
def home(request):
   return HttpResponse('<h1>Hello</h1>')

def about(request):
    contact_details = 'you can reach support at support@budgettracker.com'
    return  render(request, 'about.html',{
        'contact': contact_details
        })
    
def index(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'budget/index.html', {'categories': categories})

def expenses_view(request):
    expenses = Expense.objects.all()
    # This function will handle the request and render a response
    return render(request, 'expenses.html', {'expenses':expenses})

def add_expenses(request):
     if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the expense to the database
            return redirect('expenses')  
        else:
            print(form.errors) 
     else:
             form = ExpenseForm()
     return render(request, 'main_app/add_expenses.html', {'form':form})