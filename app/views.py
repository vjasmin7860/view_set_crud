from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet,ModelViewSet
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




    def create(self,request):
        rjd=request.data
        PDO=ProductMs(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'inserted successfully'})
        else:
            return Response({'failed':'insertion is not done please check it once'})
        


    def update(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pid=pk)
        LPO=ProductMs(instance,data=rjd)
        if LPO.is_valid():
            LPO.save()
            return Response({'updation':'is successfully done'})
        else:
            return Response({'failed':'not done check once please '})
        

    def partial_update(self,request,pk):
        rjd=request.data
        instance=Product.objects.get(pid=pk)
        LPO=ProductMs(instance,data=rjd,partial=True)
        if LPO.is_valid():
            LPO.save()
            return Response({'updation':'is successfully done'})
        else:
            return Response({'failed':'not done check once please '})
        


    def delete(self,request,pk):# it is used for delete the given instance  
        instance=Product.objects.get(pk=pk).delete()
        return Response({'delete':'deleted is successfully'})






class ProdeuctByMv(ModelViewSet):
    serializer_class=ProductMs
    queryset=Product.objects.all()


    