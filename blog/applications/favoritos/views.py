from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from applications.entrada.models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    View,
    DeleteView
)

from .models import Favorito

class UserPageView(LoginRequiredMixin,ListView):
    template_name = 'favoritos/perfil.html'
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorito.objects.entradas_user(self.request.user)
    
class AddFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        usuario = self.request.user
        entrada = Entry.objects.get(id=self.kwargs['pk'])

        Favorito.objects.create(
            user=usuario,
            entry=entrada,
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
        )


class FavoriteDeleteView(DeleteView):
    model = Favorito
    success_url = reverse_lazy('favoritos_app:perfil')
