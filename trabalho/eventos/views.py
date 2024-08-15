from django.shortcuts import render, redirect
### from django.http import HttpResponse
from .forms import EventoCulturalForm
from .models import EventoCultural

# Create your views here.
### def teste(request):
###    return HttpResponse("<h1> Aniversário de Itapajé! <h1> <p> Venha comemorar os 166 anos da nossa cidade! </p>")

def criar_evento_cultural(request):
    if request.method == 'POST':
        form = EventoCulturalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'eventos/criar_evento_cultural.html', {'form':EventoCulturalForm(), 'sucess': True})
    else:
        form = EventoCulturalForm()
    return render(request, 'eventos/criar_evento_cultural.html', {'form': form})
