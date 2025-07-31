from django.shortcuts import render,redirect,get_object_or_404
from .forms import PublisherForm,AuthorForm,BookForm
from .models import Book


# Create your views here.

def booklist(request):
    books =Book.objects.all()
    return render (request,'relation/booklist.html',{'books': books})

def addpublisher(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = PublisherForm()
    return render(request,'relation/addPublisher.html',{'form':form})

def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
            form= AuthorForm()
            return render(request,'relation/addAuthor.html',{'form':form})
        
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
            form = BookForm()
            return render(request,'relation/addbook.html',{'form':form})

def book_details(request,pk):
     book = get_object_or_404(Book,pk=pk)
     return render(request,'relation/bookdetails.html',{'book' : book})