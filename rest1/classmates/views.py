from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classmate
from .serializer import ClassmateSerializer


# Create your views here.

class ClassmateList(APIView):
    
    def get(self,request):
        classmate1 = Classmate.objects.all()
        serializer = ClassmateSerializer(classmate1, many = True)

        return Response(serializer.data)

    def post(self):
        pass