from django.db import models
from cms.models import CMSPlugin


class PessoaModel(CMSPlugin):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    funcao = models.TextField(null=True, blank=True)
    contato = models.EmailField(null=True, blank=True)

    imagem = models.ImageField(null=True, blank=True)
    lates = models.URLField(null=True, blank=True)

    info = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.nome