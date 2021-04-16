from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="BankHome"),
    path('transfer/<int:x>', views.transfer, name="transfer"),
    path('create_account/', views.create_account, name="create_account"),
    path('transfer_money/', views.transfer_money, name="transfer_money"),
    path('transaction_history/', views.transaction_history, name="transaction_history"),
    path('view/', views.view, name="View_All"),
]

