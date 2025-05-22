from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, CATEGORY_CHOICES, STATUS_CHOICES
from .forms import BookForm
from django.db.models import Q

def book_list(request):
    category = request.GET.get('category')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort', 'title')

    books = Book.objects.all()

    if category:
        books = books.filter(category=category)
    if status:
        books = books.filter(status=status)
    if sort_by:
        books = books.order_by(sort_by)

    context = {
        'books': books,
        'filter_category': category,
        'filter_status': status,
        'sort_by': sort_by,
        'category_choices': CATEGORY_CHOICES,
        'status_choices': STATUS_CHOICES,
    }
    return render(request, 'library/book_list.html', context)

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'new': True})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'new': False, 'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})