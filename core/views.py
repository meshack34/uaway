from django.shortcuts import render

# ---------- Public ----------
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page Working")

