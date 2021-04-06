from rest_framework import viewsets
from . import models
from . import serializers

class userViewset(viewsets.ModelViewSet):
    queryset = models.userModel.objects.all()
    serializer_class = serializers.userSerializer