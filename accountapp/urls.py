from django.urls import path

from accountapp.views import hello_again, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_again/', hello_again, name="Hello_again"),

    path('create/', AccountCreateView.as_view(), name="create")
]