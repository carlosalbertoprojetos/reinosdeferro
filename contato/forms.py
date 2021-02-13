from django import forms


class FormContato(forms.Form):
    # nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Nome'}))
    # email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    # mensagem = forms.CharField(label="Assunto", widget=forms.Textarea(attrs={'placeholder':'Assunto'}))
    nome = forms.CharField(label="Nome", widget=forms.TextInput())
    email = forms.EmailField(label="E-mail", widget=forms.TextInput())
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea())

