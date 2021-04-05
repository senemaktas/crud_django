#Serializers help with translating between JSON, XML, and native Python objects.

from rest_framework import serializers 
from .models import userModel
 
class userSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = userModel
        fields = ('id',
                  'name',
                  'email',
                  'phone')
