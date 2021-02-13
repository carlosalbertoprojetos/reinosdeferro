from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CriarUsuariocomEmailForm


class CadastroView(generic.CreateView):
    form_class = CriarUsuariocomEmailForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/cadastro.html'



