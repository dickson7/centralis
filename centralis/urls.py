from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('conect/<id>/', views.conect, name='conect'),
    path('connect-account/', views.connect_account, name='connect-account'),
    path('transactions/<id>/', views.transactions_account, name='transactions'),
    ]