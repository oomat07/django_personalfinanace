from django.shortcuts import render
from .models import Expense

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html', {'expenses' : expenses})

