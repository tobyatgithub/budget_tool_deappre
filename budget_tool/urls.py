"""budget_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from budgets.views import TransactionDetailView, BudgetListView, BudgetDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    # path('', TemplateView.as_view(template_name='/src/budget_tool/templates/generic/base.html'), name='home'),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('budget/', BudgetListView.as_view(), name='budget_list'),
    path('budget_detail/', BudgetDetailView.as_view(), name='budget_detail'),
    path('transaction/<int:id>', TransactionDetailView.as_view(), name='transaction_detail'),
]
