from django.shortcuts import render,redirect,get_object_or_404
from.models import Book
from.forms import FormBook


# Create your views here
def add_book(request):
    if request.method == 'POST':
        form = FormBook(request.POST)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            return render(request, 'book_list.html', {'books': books})
    else:
        form = FormBook()
    return render(request, 'add_book.html', {'form': form})
    
def book_list(request):
   books = Book.objects.all()
   return render(request, 'book_list.html', {'books':books})
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
