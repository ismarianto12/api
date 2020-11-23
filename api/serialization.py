from rest_framework import serializers
from .models import mhs, jurusan


class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model = mhs
        fields = '__all__'


class JurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = jurusan
        fields = '__all__'
