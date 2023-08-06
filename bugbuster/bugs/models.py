from django.db import models

class Bug(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Aberto', 'Aberto'),
        ('Em análise', 'Em análise'),
        ('Resolvido', 'Resolvido'),
        ('Fechado', 'Fechado')
    ])
    priority = models.CharField(max_length=50, choices=[
        ('Baixa', 'Baixa'),
        ('Normal', 'Normal'),
        ('Alta', 'Alta')
    ])
    category = models.CharField(max_length=50, choices=[
        ('Front-end', 'Front-end'),
        ('Back-end', 'Back-end'),
        ('Banco de Dados', 'Banco de Dados')
    ])
