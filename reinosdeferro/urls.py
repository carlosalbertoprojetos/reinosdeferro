from django.urls import path

from . import views
# from django.urls import reverse

# app_name = "reinosdeferro" 

# direciona para quando não houver definição de template, para home.
urlpatterns = [
    path('', views.ListaBlogView.as_view(), name='RDF'),
    path('post/novo/', views.NovoPostView.as_view(), name='novo_post'),
    path('post/<slug:slug>/', views.DetalhesBlogView.as_view(), name='detalhes_post'),
    path('post/<int:pk>/editar/', views.EditarPostView.as_view(), name='editar_post'),
    path('post/<int:pk>/deletar/', views.DeletarPostView.as_view(), name='deletar_post'),
    # path('post/<int:pk>/editar/', views.EditarPostView.as_view(), name='editar_post'),
    # o slug representa a posição do post (é possível utilizar, também, o pk)        
    # deve ficar assim no models.py (def get_absolute_url(self): return reverse('detalhes_post', arg=[self.pk]))
    # path('post/<int:pk>/', views.DetalhesBlogView.as_view(), name='detalhes_post'),

]






 