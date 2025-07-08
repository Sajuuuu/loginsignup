from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signuppage(request):
    error_message = None
   
    if request.method =='POST' :
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 != pass2 :
             error_message ="Your password and confirm password are not same!! "
        elif User.objects.filter(username=uname).exists():
            error_message = "User already exists!"
        elif User.objects.filter(email=email).exists():
            error_message = "Email already exists!"

        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')
    return render(request,'signup.html',{'error_message':error_message})
        
    



def loginpage(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']
        print(username)
        user = authenticate(request,username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('library')
        else:
         error_message = "Username or password is incorrect!!" 
        
    return render(request,'login.html',{'error_message':error_message})


def homepage(request):
    return render(request,'home.html')

# @login_required(login_url='login')
# def library(request):
#     return render (request,'library.html' )

def logoutpage(request):
    logout(request)
    return redirect('login')

    

