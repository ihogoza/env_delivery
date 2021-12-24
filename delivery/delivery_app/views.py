from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


class MedicineCreateView(GenericAPIView):
    serializer_class = MedicineSerializer
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineUpdateView(APIView):
    serializer_class = MedicineSerializer 
    def get_object(self,pk):
        try: 
                return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist: 
             raise Http404
    def get(self, request,pk, format=None):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request,pk,format=None):
        medicine=self.get_object(pk)
        serializer=MedicineSerializer(medicine,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        medicine=self.get_object(pk)
        medicine.delete()

class MakeOrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ListOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = ListOrderSerializer


        
