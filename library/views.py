from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookCreate
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@login_required(login_url = 'login')
def librarypage(request):
    user = request.user
    book_shelf = Book.objects.all()
    print(book_shelf)
    return render(request,'library.html',{'user':user, 'book_shelf':book_shelf})

def uploadform(request):
    upload = BookCreate()
    if request.method=="POST":
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('library')
        else:
            return HttpResponse("Something went wrong. Please reload")
    else:
        return render(request,'UploadForm.html',{'upload_form':upload})

def update_book(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('library')
    
    book_form = BookCreate(request.POST or None, instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('library')
    
    return render(request,'UploadForm.html',{'upload_form':book_form})

def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id=book_id)
    except:
        return redirect('library')
    book_shelf.delete()
    return redirect('library')

def send_template_email(request):
    if request.method == "POST":
        # Get values from model form
        from_email = settings.EMAIL_HOST_USER
        to_email=  request.POST['to_email']
        subject = request.POST['subject']
        body = request.POST['body']


        # Send the email
        try:
            send_mail(subject, body, from_email, [to_email])
            return render(request, 'new.html', {'message': 'Email sent successfully!'})
        except Exception as e:
            return render(request, 'new.html', {'message': f'Failed to send email: {e}'})
    else:
        return redirect('library')
    
    