from django.shortcuts import render, redirect
from .models import Clients
from django.urls import reverse


def show_list_clients(request):
    template ='clients/clients_list.html'
    clients_list = Clients.objects.filter(author=request.user.pk).order_by('pk')
    context = {
        'clients_list': clients_list
    }
    return render(request, template, context)