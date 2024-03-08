from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nom} {self.prenom}"

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def _str_(self):
        return f"{self.nom} - {self.date}"

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifiee = models.BooleanField(default=False)

    def _str_(self):
        return f"Absence de {self.etudiant} au cours de {self.cours}"

 
