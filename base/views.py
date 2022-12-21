from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# Create your views here.


@api_view()
def getRoutes(request):
    return Response(products)

@api_view(['GET'])
def getProducts(request):
    return Response(products)


@api_view(['GET'])
def getProduct(request,id):
    product = None
    for i in products:
        if i['_id'] == id:
            product=i
            break
    
    return Response(product)
