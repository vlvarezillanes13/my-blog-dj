from django.db import models

from model_utils.models import TimeStampedModel
# Create your models here.

class Home(TimeStampedModel):
    """ Model para datos de la patanlla principal"""

    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_content = models.TextField()
    about_emil = models.EmailField(
        'Email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono de contacto'
        ,max_length=20
    )

    class Meta:
        verbose_name ='Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    """ Suscriptores"""

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """ Formulario de contactor """

    full_name = models.CharField(
        'Nombres',
        max_length=50
    )
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
       return self.full_name