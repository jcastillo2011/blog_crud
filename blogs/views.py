from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView # vistas genericas
from django.urls import reverse_lazy # para redireccionar despues de crear
# la vista es donde se relacionada el template con el modelo

# Create your views here.


class PostListView(ListView):
    model = Post  # nombre del modelo donde estan los datos
    template_name = (
        "post_list.html"  # nombre del template a usar que esta en la carpeta templates
    )


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']  # Usa los campos de tu modelo
    template_name = 'post_form.html'
    success_url = reverse_lazy ('post_list')   # Redirige al listado después de crear
