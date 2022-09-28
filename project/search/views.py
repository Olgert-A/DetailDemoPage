from django.shortcuts import render
from django.http import HttpResponse

from .models import Detail, Assembly, Product, Binder


def index(request, detail_name):
    search = Binder.objects.filter(detail__detail_name=detail_name)
    active = [
        (binder.assembly,
         Product.objects.get(assembly=binder.assembly),
         binder.amount)
        for binder in search
        if binder.status == 'Act'
    ]

    print(active)

    context = {'detail': detail_name, 'active': active}
    return render(request, 'search/index.html', context)
