from django.shortcuts import render
from .models import Home 

def person_list(request):
    homes = Home.objects.all()
    return render(request, 'home.html', {'homes': homes})
    
# Create your views here.
