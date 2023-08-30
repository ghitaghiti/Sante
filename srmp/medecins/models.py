from django.db import models


class Docteurs(models.Model):
    sexe_choix = (
        ('H', 'Homme'),
        ('F', 'Femme'),
    )

    fullname= models.CharField(max_length=30)
    age=models.IntegerField()
    sexe = models.CharField(max_length=1, choices=sexe_choix)
    telephone = models.IntegerField()
    comment=models.TextField()
    image= models.ImageField(upload_to= 'photos/%d/%m/%y')
    specialitesmedicales=models.TextField()
    Anneesdepratique=models.DateField()
    Certificationsprofessionnelles=models.CharField(max_length=200)

   
class Sicks(models.Model):
    listofmaladies= (
        ("Acné","Acné" ),
        ("Alopécie","Alopécie"),
        ("Amyloïdose","Amyloïdose"),
        ("Angiodermite","Angiodermite"),
        ("Angiome stellaire","Angiome stellaire"),
        ("Anthrax staphylococcique","Anthrax staphylococcique"),
        ("Aphtose","Aphtose"),
        ("Atrophie","Atrophie"),
        ("Balanite","Balanite"),
        ("Behçet","Behçet"),
        ("Bowen","Bowen"),
        ("Carcinome basocellulaire","Carcinome basocellulaire"),
        ("Carcinome spinocellulaire","Carcinome spinocellulaire"),
        ("Candidose","Candidose"),
        ("Chancre mou","Chancre mou"),
        ("Couperose", "Couperose"),
        ("Darier", "Darier"),
        ("Degos", "Degos"),
        ("Dermatite actinique chronique", "Dermatite actinique chronique"),
        ("Dermatite herpétiforme", "Dermatite herpétiforme"),
        ("Dermatite atopique", "Dermatite atopique"),
        ("Dermatophytose", "Dermatophytose"),
        ("Dermite péri-orale", "Dermite péri-orale"),
        ("Dermite séborrhéique", "Dermite séborrhéique"),
        ("Dermographisme", "Dermographisme"),
        ("Dyshidrose", "Dyshidrose"),
        ("Eczéma", "Eczéma"),
        ("Épidermolyse bulleuse", "Épidermolyse bulleuse"),
        ("Érysipèle", "Érysipèle"),
        ("Erythema ab igne", "Erythema ab igne"),
        ("Érythème noueux", "Érythème noueux"),
        ("Érythème pigmenté fixe", "Érythème pigmenté fixe"),
        ("Érythème polymorphe", "Érythème polymorphe"),
        ("Érythrodermie", "Érythrodermie"),
        ("Erythrasma", "Erythrasma"),
        ("Escarre", "Escarre"),
    )
    lst_maladie= models.CharField(max_length=50,choices= listofmaladies)