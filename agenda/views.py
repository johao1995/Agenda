from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name='index.html'
    context={}
    return render(request,template_name,context)