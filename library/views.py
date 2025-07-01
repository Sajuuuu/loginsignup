from django.shortcuts import render


# Create your views here.
def librarypage(request):
    return render(request,'library.html')

