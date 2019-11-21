from django.shortcuts import render
from rest_framework import viewsets
from .models import Langauge
from .serializers import LangaugeSerializer

# Create your views here.

class LangaugeView(viewsets.ModelViewSet):
    queryset = Langauge.objects.all()
    serializer_class = LangaugeSerializer

    