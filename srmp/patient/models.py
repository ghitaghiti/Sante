from django.db import models

from django.db import models


class Patient(models.Model):
    fullname= models.CharField(max_length=30)
    age=models.IntegerField()
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    telephone = models.CharField(max_length=20)
    symptom=models.CharField( max_length=100)
   
 