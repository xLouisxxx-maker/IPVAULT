from django.shortcuts import render, HttpResponse
from .models import Patent
def home(request):
    return render(request, "home.html")
#load html

def patents(request):
    items = Patent.objects.all()
    return render(request, "patents.html", {"patents": items})
#view renders all patens there is