from django.shortcuts import render
from django.http import HttpResponse

# Define the home view function
def home(request):
   return HttpResponse('<h1>Hello</h1>')

def about(request):
    contact_details = 'you can reach support at support@budgettracker.com'
    return  render(request, 'about.html',{
        'contact': contact_details
        })