from rest_framework import serializers
from .models import Langauge

class LangaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langauge
        fields = ('id', 'name', 'paradigm')

    

