from applications.entrada.models import Entry
from django.conf import settings
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

class Favorito(TimeStampedModel):
    """ Modelo para favoritos """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user','entry')
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'

    def __str__(self):
        return self.entry.title