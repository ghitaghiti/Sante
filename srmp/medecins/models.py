from django.db import models


class Docteurs(models.Model):
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )

    fullname= models.CharField(max_length=30)
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    telephone = models.IntegerField(max_length=30)
    image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    specialitesmedicales=models.TextField()
    Anneesdepratique=models.DateField()
    
    def __str__(self):
        return self.fullname

