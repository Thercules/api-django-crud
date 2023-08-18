# models.py

from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outros', 'Outros')
    ]
    nomecompleto = models.CharField('Nome Completo', max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)  
    nascimento = models.DateField('Data de Nascimento')
    whatsapp = models.CharField('Whatsapp', max_length=15)
    email = models.EmailField('Email')
    sexo = models.CharField('Sexo', max_length=9, choices=SEXO_CHOICES)
    ativo = models.BooleanField('Ativo', default=True)  
    endereco = models.CharField('Endereço', max_length=150)
    cep = models.CharField('CEP', max_length=10, default='')  
    estado = models.CharField('Estado', max_length=50, default='')  
    cidade = models.CharField('Cidade', max_length=100, default='')  
    bairro = models.CharField('Bairro', max_length=100, default='')  
    logradouro = models.CharField('Logradouro', max_length=255, default='') 
    numero = models.CharField('Número', max_length=10, default='')  

    def __str__(self):
        return self.nomecompleto
