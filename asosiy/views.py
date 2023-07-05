from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from django.contrib.postgres.search import TrigramSimilarity

class QoshiqchilarAPIView(APIView):
    def get(self, request):
        qoshiqchlar = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchlar, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self,request):
        qoshiqchi = request.data
        serializer = QoshiqchiSerializer(data=qoshiqchi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QoshiqchiDetalView(APIView):
    def get(self , request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        Qoshiqchi.objects.get(id=pk).delete()
        return Response({"xabar":"Qoshiqchi ma'lumoti o'chirildi."}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id = pk)
        malumot = request.data
        serializer = QoshiqchiSaveSerializer(qoshiqchi, data = malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QoshiqDetalView(APIView):
    def get(self , request, pk):
        qoshiqchi = Qoshiq.objects.get(id=pk)
        serializer = QoshiqSerializer(qoshiqchi)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        Qoshiq.objects.get(id=pk).delete()
        return Response({"xabar":"Qoshiq ma'lumoti o'chirildi."}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        qoshiq = Qoshiq.objects.get(id = pk)
        malumot = request.data
        serializer = QoshiqSaveSerializer(qoshiq, data = malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)