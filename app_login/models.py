from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError

class Cadastro(AbstractBaseUser):
    nome_usuario = models.CharField(max_length=30, unique=True)
    email_usuario = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    confirmacao_senha = models.CharField(max_length=128)

    USERNAME_FIELD = 'nome_usuario'
    EMAIL_FIELD = 'email_usuario'
    REQUIRED_FIELDS = ['email_usuario']

    def __str__(self):
        return self.nome_usuario

    def clean(self):
        # Verificar se a senha e a confirmação da senha são iguais
        if self.senha != self.confirmacao_senha:
            raise ValidationError("As senhas não são iguais")

    def save(self, *args, **kwargs):
        # Gerar a senha hash usando o método set_password
        self.set_password(self.senha)
        super().save(*args, **kwargs)
