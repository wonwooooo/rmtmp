from django.shortcuts import render

# Create your views here.

import sqlite3
from .models import Company, Client, Product, Order
from django.http import JsonResponse, HttpResponse, Http404
import datetime, json


def client(request):
    if request.method == "GET":
        client_list = []
        client = Client.objects.all()

        total_client = 0
        for c in client:
            phone_number = c.client_phone_number.replace(c.client_phone_number[-3:-1], '**')
            client_list.append({"clinet_id" : c.id ,
                                "client_name" : c.client_name,
                                "clinet_phone" : phone_number})
            total_client += 1
        return JsonResponse({"total_client" : total_client , "list" : client_list} , safe=False)


def company(request):
    if request.method == "GET":
        company_list = []
        company = Company.objects.all()

        total_company = 0
        for c in company:
            company_list.append({"company_id" : c.id, 
                                 "company_name" : c.company_name, 
                                 "company_boos_name" : c.company_boss_name, 
                                 "company_phone_number" : c.company_phone_number})
            total_company += 1
        return JsonResponse({"total_company" : total_company, "list" : company_list}, safe=False)


def product(request):
    if request.method == "GET":
        product_list = []
        product = Product.objects.all()

        print(product)

        total_product = 0
        for p in product:
            product_list.append({"product_id" : p.id, 
                                 "product_name" : p.p_name, 
                                 "product_price" : p.p_price, 
                                 "product_registerdate" : p.p_registerdate.strftime('%Y-%m-%d-%H-%M-%S'), 
                                 "product_company_name" : p.p_company_name})

            total_product += 1
        return JsonResponse({"total_product" : total_product, "list" : product_list}, safe=False)



# def order(request):
#     if request.method == "GET":
#         order_list = []
#         order = Order.objects.all()

#         for o in order:
#             order_list.append({컬럼1 : o.id
#                                 컬럼2 : 컬럼이름값,실제값})
#             total_order += total_order
#         return JsonResponse({고정된형태})