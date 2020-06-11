from django.db import models
from django.core.validators import validate_email, validate_ipv4_address
from django.core.validators import MinLengthValidator

# Validador da senha para que tenha no mínimo 8 caracteres.
validate_password = MinLengthValidator(
    8, "Deve possuir pelo menos 8 caracteres!")


# Modelo da Tabela do Usuário
class User(models.Model):
    name = models.CharField(max_length=50)
    # auto_now = True para cada vez que um registro é salvo,
    # ele é atualizado para a hora atual
    last_login = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=254, validators=[validate_email])
    password = models.CharField(max_length=50, validators=[validate_password])


# Modelo da Tabela do Agente
class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.CharField(
        max_length=39,
        validators=[validate_ipv4_address]
    )


# Classe para definir as opções do nível do evento
class Level(models.TextChoices):
    CRITICAL = 'CRITICAL', 'CRITICAL'
    DEBUG = 'DEBUG', 'DEBUG'
    ERROR = 'ERROR', 'ERROR'
    WARNING = 'WARNING', 'WARNING'
    INFO = 'INFO', 'INFO'


# Modelo da Tabela do Evento
class Event(models.Model):
    level = models.CharField(
        max_length=20, choices=Level.choices,
        default=Level.INFO
    )
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

# Modelo da Tabela do Grupo
class Group(models.Model):
    name = models.CharField(max_length=50)


# Modelo da Tabela de Relacionamento entre Grupo e Usuário
class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )
