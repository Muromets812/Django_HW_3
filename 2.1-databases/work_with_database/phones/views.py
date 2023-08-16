from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog_view(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product_view(request, re_slug):
    phone = get_object_or_404(Phone, slug=re_slug)

    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
