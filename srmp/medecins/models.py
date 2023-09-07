from django.db import models


class Docteurs(models.Model):
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )

    fullname= models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    adresse=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    telephone = models.IntegerField()
    image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    specialitesmedicales=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.fullname


class DocteurSignUp(models.Model):
    last_login = models.DateTimeField(auto_now=True)
    fullname= models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=128, default='')
    password2 = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.fullname
