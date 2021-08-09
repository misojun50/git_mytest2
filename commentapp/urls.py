from django.urls import path

from commentapp.views import CommentCreationView

app_name = 'commentapp'

urlpatterns = [

    path('create/', CommentCreationView.as_view(), name='create'),

]