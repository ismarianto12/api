from rest_framework import serializers
from .models import mhs 

class SerializationClass(serializers.ModelSerializer):
            class Meta:
                model=mhs
                fields='__all__'