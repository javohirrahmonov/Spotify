from datetime import timedelta
from rest_framework import serializers
from .models import Qoshiqchi, Albom, Qoshiq
from django.test import TestCase

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class QoshiqchiSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'


class AlbomSerializer(serializers.ModelSerializer):
    qoshiqchi = QoshiqchiSerializer()

    class Meta:
        model = Albom
        fields = '__all__'

class QoshiqSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()

    class Meta:
        model = Qoshiq
        fields = '__all__'

class QoshiqSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self,qiymat):
        if qiymat.endswith(".mp3") == True:
            return qiymat
        raise serializers.ValidationError(".mp3 bolishi shart!")

    def validate_davomiylik(self,qiymat):
        max_duration = timedelta(minutes=7)
        if qiymat and qiymat > max_duration:
            raise serializers.ValidationError("The duration should not exceed 00:07:00.")
        return qiymat

