from django.db import models

class Lkhra(models.Model):
    villeslist= [
        ('Oujda', 'oujda'),
        ('fes', 'fes'),
        ('casa', 'casa'),
    ]
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    villes=models.CharField(max_length=50, choices= villeslist)
    
    # def __str__(self) -> str:
    #     return self.username
