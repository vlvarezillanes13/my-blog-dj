from applications.favoritos.models import Favorito
from django.contrib import admin

# Register your models here.


class FavoritoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'entry',
     )

admin.site.register(Favorito,FavoritoAdmin)