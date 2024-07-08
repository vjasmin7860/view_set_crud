from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import *
from app.serializers import *



class ProductCrud(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()#list product objects 
        JPO=ProductMs(LPO,many=True)#model serializers product object
        return Response(JPO.data)
    


    def retrieve(self,request,pk):
        PO=Product.objects.get(pid=pk)
        JO=ProductMs(PO)
        return Response(JO.data)

    