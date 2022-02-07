from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey()
    usuario_comentario = models
    data_comentario = models
    publicado_comentario = models
