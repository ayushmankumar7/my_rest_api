from rest_framework import serializers
from .models import Classmate

class ClassmateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Classmate
        fields = '__all__'
