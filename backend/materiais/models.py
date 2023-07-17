from datetime import datetime, timezone
from stdimage import StdImageField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'masculino'),
        ('M', 'feminina'),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    email = models.EmailField(unique=True)
    foto = StdImageField(
        blank=True,
        upload_to='user/',
        # estamos definindo uma variação de miniatura com largura e altura de 100 pixels e a opção de recorte (crop).
        variations={
            'thumbnail': {
                'width': 100,
                'height': 100,
                'crop': True
            }
        },
        # garantir que apenas arquivos com as extensões 'jpg', 'jpeg' e 'png' sejam permitidos.
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    # para criar uma senha criptografada antes de salvar o usuário:
    def save(self, *args, **kwargs):
        # # Verifica se a senha foi alterada ou é uma nova instância
        # if self.pk is None or self._state.adding or 'password' in self.get_dirty_fields():
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    # função de sinal que será acionada quando um usuário fizer login. Essa função atualizará o campo last_login para a data e hora atual:
    def update_last_login(sender, user, request, **kwargs):
        user.last_login = datetime.utcnow()
        user.save()

    # Registrar a função de sinal para o sinal 'user_logged_in'
    user_logged_in.connect(update_last_login)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_permissions',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    def __str__(self) -> str:
        return self.username


class Material(models.Model):
    TIPOS_MATERIAIS = (
        ('E', 'Electrônico'),
        ('P', 'Papelaria'),
        ('F', 'Ferramentas'),
        ('ES', 'Equipamentos de segurança'),
        ('PL', 'Produtos de limpeza'),
        ('M', 'Mobiliário'),
        ('EI', 'Equipamentos de informática'),
        ('MC', 'Materiais de construção'),
        ('UC', 'Utensílios de cozinha'),
        ('AE', 'Artigos esportivos'),
        ('IM', 'Instrumentos musicais'),
        ('O', 'Outros')
    )
    tipo = models.CharField(choices=TIPOS_MATERIAIS, default='O', max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = StdImageField(
        # o caminho onde as imagens serão salvas.
        upload_to='materiais/',
        # estamos definindo uma variação de miniatura com largura e altura de 100 pixels e a opção de recorte (crop).
        variations={
            'thumbnail': {
                'width': 100,
                'height': 100,
                'crop': True
            }
        },
        # garantir que apenas arquivos com as extensões 'jpg', 'jpeg' e 'png' sejam permitidos.
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
