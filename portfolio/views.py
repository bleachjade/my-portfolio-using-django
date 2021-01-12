from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Info

def index(request):
    info = Info.objects.all()
    return render(request, 'portfolio/index.html', {'info': info})
    
