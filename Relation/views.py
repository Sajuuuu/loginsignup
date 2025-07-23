from django.shortcuts import render,redirect
from .forms import PublisherForm
from .models import Book

# Create your views here.

def booklist(request):
    books =Book.object.all()
    return render (request,'relation/booklist.html',{'books': books})

def addpublisher(request):
    if request.method == "POST":
        form =PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
        else:
            form = PublisherForm()
            return render(request,'relation/addPublisher.html',{'form':form})


