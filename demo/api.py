from rest_framework import generics
from rest_framework.response import Response
from .serializer import userSerializer
from .models import userModel

class userCreateApi(generics.CreateAPIView):
    queryset = userModel.objects.all()
    serializer_class = userSerializer

class userApi(generics.ListAPIView):
    queryset = userModel.objects.all()
    serializer_class = userSerializer

class userUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = userModel.objects.all()
    serializer_class = userSerializer

class userDeleteApi(generics.DestroyAPIView):
    queryset = userModel.objects.all()
    serializer_class = userSerializer
