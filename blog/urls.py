from django.urls import path
from . import views  # Importa todas as views do app blog

urlpatterns = [
    # Rota principal - lista todos os posts
    path('', views.post_list, name='home'),

    # Rota de detalhe - exibe um post específico pelo seu ID
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # Rota de criação - exibe o formulário para criar um novo post
    path('post/new/', views.post_new, name='post_new'),

    # Rota de edição - exibe o formulário para editar um post existente
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # Rota de exclusão - exibe a confirmação para deletar um post
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]