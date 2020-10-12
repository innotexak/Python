from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateBook
from .models import Book
from django.contrib import messages


# THis is the view function to all my objects in the database 
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/index.html', {'shelf': shelf})

def upload_form(request):
    upload = CreateBook()
    if request.method == "POST":
        upload = CreateBook(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" Your form is invalid, please click to <a href={{url:'upload'}}>Reload</a>""")


    else:
        return render(request, 'book/my_form.html', {'my_form': upload})

def update(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    update_form = CreateBook(request.POST or None, instance=book_sel)
    if update_form.is_valid():
        update_form.save()
        return redirect('index')
    return render(request, 'book/my_form.html', {'my_form': update_form})

def delete(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    messages.success(request, "Your book is deleted succesfully")
    return redirect('index')
    


