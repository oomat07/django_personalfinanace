from django.shortcuts import render
from .models import Income
from django.views.generic.edit import CreateView
from .forms import IncomeForm
from django.urls import reverse_lazy

def incomes_list(request):
    incomes = Income.objects.all()
    return render(request, 'incomes_list.html', {'incomes' : incomes})


class IncomeCreateView(CreateView):
    model = Income
    template_name = 'create_income.html'
    form_class = IncomeForm
    success_url = reverse_lazy('incomes_list')