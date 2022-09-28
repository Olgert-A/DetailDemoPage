from django.shortcuts import render
from django.http import HttpResponse

from .models import Detail, Assembly, Product, Binder


def index(request, detail_name):
    search = Binder.objects.filter(detail__detail_name=detail_name)
    active = [binder for binder in search if binder.status == 'Act']
    archive = [binder for binder in search if binder.status == 'Arc']
    context = {'detail': detail_name, 'active': active, 'archive': archive}
    return render(request, 'search/index.html', context)
