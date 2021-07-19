from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_again, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('hello_again/', hello_again, name="Hello_again"),

    path('create/', AccountCreateView.as_view(), name="create"),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),name='login'),

    path('logout/', LogoutView.as_view(),name='logout'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('detele/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]