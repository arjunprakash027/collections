from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
class BasicsApi(APIView):
    def get(self,request):
        return Response({"message":"Hello world"})

class AsmallComputation(APIView):
    def get(self,request,a,b):
        c = a+b
        return Response({"Computation":c})

class AsmallComputation2(APIView):
    def get(self,request):
        a = int(request.GET.get("a"))
        b = int(request.GET.get("b"))
        c = a+b
        return Response({"Computation":c})

