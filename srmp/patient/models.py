from django.db import models

from django.db import models


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fullname= models.CharField(max_length=30)
    age=models.IntegerField()
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    telephone = models.CharField(max_length=20)
    admit=models.BooleanField(default=True)
    commnt=models.TextField()
    image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    specialitesmedicales=models.TextField()
    Anneesdepratique=models.DateField()
    Certificationsprofessionnelles=models.CharField(max_length=200)
 