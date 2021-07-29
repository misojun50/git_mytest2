from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloAgain
from accountapp.decorators import account_validation


@login_required
def hello_again(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        hel_again = HelloAgain()
        hel_again.text = temp
        hel_again.save()

        return HttpResponseRedirect(reverse("accountapp:Hello_again"))
    else:
        hel_again_list = HelloAgain.objects.all()
        return render(request, 'accountapp/hello_again.html',
                      context={'hel_again_list': hel_again_list })


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:Hello_again')
    template_name ='accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_User'
    template_name = 'accountapp/detail.html'

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
    success_url = reverse_lazy('accountapp:Hello_again')
    template_name = 'accountapp/delete.html'