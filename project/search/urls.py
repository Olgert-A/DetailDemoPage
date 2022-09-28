from django.urls import path

from . import views

urlpatterns = [
    path('<str:detail_name>/', views.index, name='index')
]
