# I have created this file - Darshan
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
