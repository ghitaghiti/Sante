from django.db import models

class Maladie(models.Model):
    names=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.names

class Villes(models.Model):

    names= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.names
    
