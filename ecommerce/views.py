from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import OrderSerializer
from .models import Orders

# Create your views here.

@api_view(["GET", "POST"])
def post_get(request):
    if request.method == "GET":
        order = Orders.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def update_link(request, id):
    try:
        ordersinfo = Orders.objects.get(pk=id)
    except ordersinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrderSerializer(ordersinfo)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = OrderSerializer(ordersinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        ordersinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
