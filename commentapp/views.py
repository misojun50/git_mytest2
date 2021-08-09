from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreationView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.article.pk})
