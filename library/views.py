from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book


# Create your views here.
@login_required(login_url = 'login')
def librarypage(request):
    user = request.user
    book_shelf = Book.objects.all()
    print(book_shelf)
    return render(request,'library.html',{'user':user, 'book_shelf':book_shelf})

def uploadform(request):
    return render(request,'uploadform.html')
