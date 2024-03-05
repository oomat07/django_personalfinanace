from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

def expenses_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html', {'expenses' : expenses})

class ExpenseCreateView(CreateView):
    model = Expense
    template_name = 'create_expenses.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses')

class ExpenseDetailView(DetailView):
    model = Expense
    context_object_name = 'expense'
    template_name = 'expense_detail.html'