from django.shortcuts import render

def signuppage(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

# Create your views here.
