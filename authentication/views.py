from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication import serializers
from rest_framework import response, status, permissions
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.


# class AuthUserAPIView(GenericAPIView):

#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request):
#         user = request.user
#         serializer = RegisterSerializer(user)
#         return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['password']= make_password(serializer.validated_data.get("password"))
            serializer.save()
            return response.Response(serializer.data, status= status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status= status.HTTP_200_OK)
        return response.Response({"message": "Invalid username or password"}, status= status.HTTP_401_UNAUTHORIZED)