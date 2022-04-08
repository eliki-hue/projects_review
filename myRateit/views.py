from django.shortcuts import render

# Create your views here.

def home(request):
    message ='Welcome to rateit'
    return render(request, 'index.html',{'message': message})