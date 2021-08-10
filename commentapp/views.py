from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_owner_var
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreationView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_owner_var, 'get')
@method_decorator(comment_owner_var, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name ='target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk':self.object.article.pk})