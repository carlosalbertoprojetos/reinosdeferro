from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget



class PostForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('titulo', 'conteudo', 'categoria', 'imagem', 'status') 

