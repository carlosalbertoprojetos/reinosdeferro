from django.urls import path
from . import views
from django.urls import reverse

urlpatterns = [
    path('cadastro/', views.CadastroView.as_view(), name='Cadastro'),
]

