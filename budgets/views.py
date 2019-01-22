from django.urls import reverse_lazy
from .models import Budget, Transaction
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BudgetListView(ListView):
    """
    List all available budgets owned by current user.
    """
    template_name = '/src/budgets/templates/budget/budget_list.html'
    context_object_name = 'budgets'
    # login_url = reverse_lazy('login')

    def get_queryset(self):
        # pass
        return Budget.objects.filter(user__username=self.request.user.username)
        # return Budget.objects.all()

    def get_context_data(self, **kwargs):
        # pass
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context
        # return Budget.objects.all()


class BudgetDetailView(ListView):
    """
    List all available budgets owned by current user.
    """
    template_name = '/src/budgets/templates/budget/budget_detail.html'
    context_object_name = 'budgets'
    # login_url = reverse_lazy('login')

    def get_queryset(self):
        # pass
        return Budget.objects.filter(user__username=self.request.user.username)
        # return Budget.objects.all()

    def get_context_data(self, **kwargs):
        # pass
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context
        # return Budget.objects.all()


class TransactionDetailView(DetailView):
    """
    List all available transactions within the selected budget.
    """
    template_name = '/src/budgets/templates/budgets/transaction_detail.html'
    model = Transaction
    context_object_name = 'transaction'
    # login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        # return Transaction.objects.all()
        return Budget.objects.filter(user__username=self.request.user.username)