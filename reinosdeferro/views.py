from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# algumas aplicações serão permitidas apenas se o autor estiver logado utilizando LoginRequiredMixin para class e @login_required para def
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ListaBlogView(ListView):
    model = Post
    template_name = 'reinosdeferro/rdf.html'

class DetalhesBlogView(DetailView):
    model = Post
    template_name = 'reinosdeferro/detalhes_post.html'

# LoginRequiredMixin faz com que seja necessário estar logado para criar um novo post
class NovoPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'reinosdeferro/novo_post.html'
    form_class = PostForm
    success_message = 'Cadastrado com sucesso!'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

# LoginRequiredMixin faz com que seja necessário estar logado para criar um novo post
class EditarPostView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'reinosdeferro/editar_post.html'
    success_message = 'Editado com sucesso!'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

# LoginRequiredMixin faz com que seja necessário estar logado para criar um novo post
class DeletarPostView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'reinosdeferro/deletar_post.html'
    success_url = reverse_lazy('RDF')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(DeletarPostView, self).delete(request, *args, **kwargs)


