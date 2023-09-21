from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez ici d'autres champs spécifiques à votre modèle UserProfile
    # Par exemple, vous pourriez avoir un champ pour le numéro de téléphone
    
    def __str__(self):
        return self.user.username



class users(models.Model):
	user = models.ForeignKey(User, related_name="code", on_delete=models.DO_NOTHING)
	symptoms = models.TextField(max_length=5000)
	Recommander = models.TextField(max_length=5000)
	villes = models.CharField(max_length=50)


	def __str__(self):
		return self.question