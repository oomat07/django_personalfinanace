from django.urls import path
from .import views
urlpatterns = [
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('expenses/add/', views.ExpenseCreateView.as_view(), name='create_expenses'),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expenses_detail')
]