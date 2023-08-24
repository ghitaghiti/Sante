from django.db import models


class Docteurs(models.Model):
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )

    #id = models.AutoField(primary_key=True)
    fullname= models.CharField(max_length=30)
    age=models.IntegerField()
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    telephone = models.IntegerField()
    comment=models.TextField()
    image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    specialitesmedicales=models.TextField()
    Anneesdepratique=models.DateField()
    Certificationsprofessionnelles=models.CharField(max_length=200)
