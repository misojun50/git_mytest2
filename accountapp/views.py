from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloAgain
from accountapp.decorators import account_validation
from articleapp.models import Article


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name ='accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_User'
    template_name = 'accountapp/detail.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)

account_var = [login_required, account_validation]

@method_decorator(account_var, 'get')
@method_decorator(account_var, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_User'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.pk})

@method_decorator(account_var, 'get')
@method_decorator(account_var, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_User'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'