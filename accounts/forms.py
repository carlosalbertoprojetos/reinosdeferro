from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# insere um campo para armazenar emails
class CriarUsuariocomEmailForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Campo obrigatório! Insira um email válido!')
    # foto = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email',)

    # validação - verificar se o email informado para cadastrado já existe
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está cadastrado, por favor insira outro.')
        return email


