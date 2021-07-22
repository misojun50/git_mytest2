from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_validation(func):
    def wrap(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrap