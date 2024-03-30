from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Filmes(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField(max_length=70)
    data = models.DateField()
    foto = models.ImageField(blank=True, upload_to= 'posters/')
    nota_media = models.FloatField(blank=True, null=True)
    review = models.TextField(max_length=150)
    def __str__(self):
        return f'{self.nome}'
    
class Reviews(models.Model):
    filme = models.ForeignKey(Filmes, on_delete=models.CASCADE)
    review = models.TextField(max_length=150)
    nota = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(10,0)])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    def __str__(self):
        return f'{self.user.username} {self.filme} {self.nota}'

@receiver(pre_save, sender=Reviews)
def set_contact_owner(sender, instance, **kwargs):
        if not instance.usuario_id:
            instance.usuario = instance._request_user





