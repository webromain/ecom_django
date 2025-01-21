from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'siteecom/home.html')
