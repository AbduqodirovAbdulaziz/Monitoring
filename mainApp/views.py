from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import *
from .serializer import *
from .models import *


class XaridorApiView(APIView):
    def get(self, request):
        xaridor = Xaridor.objects.all()
        serializer = XaridorSerializer(xaridor, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=XaridorSerializer,
    )
    def post(self, request):
        serializer = XaridorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Ma'lumot qo'shildi"})
        return Response(serializer.errors)


class XaridorEditApiView(APIView):
    def get(self, request, pk):
        xaridor = get_object_or_404(Xaridor, id=pk)
        serializer = XaridorSerializer(xaridor, data=request.data)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=XaridorSerializer,
    )
    def put(self, request, pk):
        xaridor = get_object_or_404(Xaridor, id=pk)
        serializer = XaridorSerializer(xaridor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messagee": "ma'lumot tahrirlandi"})
        return Response(serializer.errors)

    def delete(self, request, pk):
        xaridor = get_object_or_404(Xaridor, id=pk)
        xaridor.delete()
        return Response({"success": "Ma'lumot o'chirildi"})


class SotuvApiView(APIView):
    def get(self, request):
        sotuv = Sotuv.objects.all()
        serializer = SotuvSerializer(sotuv, many=True)
        return serializer.data

    @swagger_auto_schema(
        request_body=SotuvSerializer,
    )
    def post(self, request):
        serializer = SotuvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Ma'lumot qo'shildi"})
        return Response(serializer.errors)


class SotuvEdit(APIView):
    def get(self, request, pk):
        sotuv = get_object_or_404(Sotuv, id=pk)
        serializer = SotuvSerializer(sotuv)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=SotuvSerializer,
    )
    def put(self, request, pk):
        sotuv = get_object_or_404(Sotuv, id=pk)
        serializer = SotuvSerializer(sotuv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "updated_data": serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        sotuv = get_object_or_404(Sotuv, id=pk)
        sotuv.delete()
        return Response({"success": "ma'lumot o'chirildi"})


class XarajatlarApiView(APIView):
    def get(self, request):
        xarajat = Xarajatlar.objects.all()
        serializer = XarajatlarSerializer(xarajat, many=True)
        return serializer.data

    @swagger_auto_schema(
        request_body=XarajatlarSerializer,
    )
    def post(self, request):
        serializer = XarajatlarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Ma'lumot qo'shildi"})
        return Response(serializer.errors)


class XarajatlarEditApiView(APIView):
    def get(self, request, pk):
        xarajat = get_object_or_404(Xarajatlar, id=pk)
        serializer = XarajatlarSerializer(xarajat)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=XarajatlarSerializer,
    )
    def put(self, request, pk):
        xarajat = get_object_or_404(Xarajatlar, id=pk)
        serializer = XarajatlarSerializer(xarajat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "updated_data": serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        xarajat = get_object_or_404(Xarajatlar, id=pk)
        xarajat.delete()
        return Response({"message": "ma'lumot o'chirildi"})
