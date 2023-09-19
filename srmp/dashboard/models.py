from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez ici d'autres champs spécifiques à votre modèle UserProfile
    # Par exemple, vous pourriez avoir un champ pour le numéro de téléphone
    
    def __str__(self):
        return self.user.username