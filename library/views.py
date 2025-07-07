from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = 'login')
def librarypage(request):
    user = request.useer
    return render(request,'library.html',{'user':user})

def uploadform(request):
    return render(request,'uploadform.html')
