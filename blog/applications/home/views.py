import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)

from applications.entrada.models import Entry

from applications.home.models import Home
from applications.home.forms import ContactForm, SuscribersForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        #Home
        context["home"] = Home.objects.latest('created')
        #Contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #Contextos para articulos en el home
        context["entradas_home"] = Entry.objects.entrada_en_home()
        #Contextos para articulos recientes
        context["entradas_recientes"] = Entry.objects.entrada_recientes()

        #Formulario suscripcion
        context['form'] = SuscribersForm
        return context
    


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'

