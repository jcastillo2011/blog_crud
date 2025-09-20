from django.shortcuts import render
from .models import Post
from django.views.generic import ListView  #vistas genericas

#la vista es donde se relacionada el template con el modelo

# Create your views here.

class PostListView(ListView):
    model = Post  #nombre del modelo donde estan los datos
    template_name = 'post_list.html' #nombre del template a usar que esta en la carpeta templates
    