from pprint import pprint
from django.shortcuts import render, redirect
from phones.models import Phone

def _sort_phones(sorting_rule, phones):
    if sorting_rule == 'name':
        return phones.order_by('name')
    elif sorting_rule == 'min_price':
        return phones.order_by('price')
    elif sorting_rule == 'max_price':
        return phones.order_by('-price') # '-' before indicates DESCending order

def index(request):
    return redirect('catalog')

def show_catalog(request):
    sorting_rule = request.GET.get('sort', 'name')
    phones = Phone.objects.all()
    sorted_phones = _sort_phones(sorting_rule=sorting_rule, phones = phones)
    template = 'catalog.html'
    context = { 'phones': sorted_phones }
    return render(request, template, context)

def show_product(request, slug):
    #As slug is a unique field, the only object will be returned by manager
    phones = Phone.objects.filter(slug = slug)
    phone = phones[0]
    template = 'product.html'
    context = { 'phone': phone }
    return render(request, template, context)
