from django.shortcuts import render
from apps.Incomes.models import Income
from apps.Expenses.models import Expense
from django.db.models import Sum

def finacial_summary(request):
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    context = {
        'total_income' : total_income,
        'total_expence' : total_expense,
        'net' : total_income - total_expense
    }
    return render(request, 'financial_summary.html', context)

