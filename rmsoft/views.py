from django.shortcuts import render

# Create your views here.

import sqlite3
from .models import Company, Client, Product, Order
from django.http import JsonResponse, HttpResponse, Http404


def client(request):
    if request.method == "GET":
        client_list = []
        client = Client.objects.all()

        total_client = 0
        for c in client:
            client_list.append({"clinet_id" : c.id ,
                                "client_name" : c.client_name,
                                "clinet_phone" : c.client_phone_number})
            total_client = total_client+1
        return JsonResponse({"total_client" : total_client , "list" : client_list} , safe=False)
