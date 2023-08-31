from django.db import models


class Docteurs(models.Model):
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )

    Nom_Complete= models.CharField(max_length=30)
    Adresse=models.TextField()
    Sexe = models.CharField(max_length=1, choices=sexe_choix)
    Telephonee = models.CharField(max_length=20)
    Image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    Specialites_medicales=models.TextField()
    Annees_de_Pratique=models.DateField()
    Certifications_professionnelles=models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.Nom_Complete
   
