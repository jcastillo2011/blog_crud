from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # toma el tiempo automaticament del sistem o pc
    updated_at = models.DateTimeField(auto_now=True) # toma el tiempo automaticament del sistem o pc
    author = models.ForeignKey(
                            'auth.User', on_delete=models.CASCADE
                            ) # toma el usario de la tabla auth_user de la base de datos de usuario por defecos de django
    def __str__(self): 
        return self.title




