from django.urls import reverse_lazy
from .models import Budget, Transaction
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BudgetListView(ListView):
    """
    List all available budgets owned by current user.
    """
    template_name = '/src/budgets/templates/budget/budget_list.html'
    context_object_name = 'budgets'  # this will be the reference for the get_queryset() result
    # login_url = reverse_lazy('login')

    def get_queryset(self):
        # this line will be translated to SQL when called and filter is completed at database level.
        # this is way more efficient compared to query everything in sql, get to python and process
        # at python level.
        return Budget.objects.filter(user__username=self.request.user.username)
        # return Budget.objects.all()

    # def get_context_data(self, **kwargs):
    #     # 1. inherite information from super class (e.g. token, context object name, etc.)
    #     context = super().get_context_data(**kwargs)  
    #     # 2. we add one more info onto our context
    #     # budget__user__username -> in database, budget has an attr called user with an attr called username
    #     context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
    #     return context
    #     # return Budget.objects.all()


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
        # 1. inherite information from super class (e.g. token, context object name, etc.)
        context = super().get_context_data(**kwargs)  
        # 2. we add one more info onto our context
        # budget__user__username -> in database, budget has an attr called user with an attr called username
        context['transactions'] = Transaction.objects.filter(budget__user__username=self.request.user.username)
        return context
        # return Budget.objects.all()


class TransactionDetailView(DetailView):
    """
    List all available transactions within the selected budget.
    """
    template_name = '/src/budgets/templates/budgets/transaction_detail.html'
    model = Transaction  # == to assign value to self.model
    context_object_name = 'transaction'
    # login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    # def get_queryset(self):
    #     # here we don't want info from super class.
    #     return Budget.objects.filter(assign_to__username=self.request.user.username)
    #     # return Transaction.objects.filter(assign_to == something)
    #     # return Budget.objects.filter(user__username=self.request.user.username)


class BudgetCreateView(LoginRequiredMixin, CreateView):
    pass


class TransactionCreateView(LoginRequiredMixin, CreateView):
    pass