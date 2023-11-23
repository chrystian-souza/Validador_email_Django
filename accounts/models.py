from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=14, blank=True, unique=True)
    idade = models.IntegerField(blank=True, default=0)
    data_nascimento = models.DateField(blank=True, default=datetime.now())

    USERNAME_FIELD = 'cpf'
    

