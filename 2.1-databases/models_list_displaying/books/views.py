from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_list_view(request):
    template = 'books/books_list.html'
    context = {}

    book_list = Book.objects.all().order_by('pub_date')

    context['page_obj'] = book_list
    return render(request, template, context)


def books_by_date_view(request, pub_date):
    books_objects = Book.objects.filter(pub_date__exact=pub_date)
    previous_page = Book.objects.filter(pub_date__lt=pub_date).first()
    next_page = Book.objects.filter(pub_date__gt=pub_date).first()
    template = 'books/books_by_date.html'
    context = {
        'books': books_objects,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)
