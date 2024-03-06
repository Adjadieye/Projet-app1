from django.shortcuts import render
from django.http import HttpResponse
from .models import Etudiant, Cours, Absence

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'absences/liste_etudiants.html', {'etudiants': etudiants})

def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'absences/liste_cours.html', {'cours': cours})

def enregistrer_absence(request):
    # Ajoutez le code pour enregistrer une absence ici
    return render(request, 'absences/enregistrer_absence.html')


# Create your views here.
