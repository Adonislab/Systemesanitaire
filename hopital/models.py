from django.db import models


class Depot(models.Model):

    def __str__(self):
        return f'{self.nom_du_produit}'

    class categorie(models.TextChoices):
        Pharmaceutique = 'Pharmaceutique'
        Magazin = 'Magazin'
        Banque_de_sang = 'Banque de sang'
        Laboratoire = 'Laboratoire'
        Depot_repartiteur = 'Depot repartiteur'

    type_du_produit = models.fields.CharField(max_length=20, choices=categorie.choices)
    nom_du_produit = models.fields.CharField(max_length=20)
    nombre_de_stoke = models.fields.IntegerField()
    prix_unitaire = models.fields.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)



class RessourceHumaine(models.Model):

    def __str__(self):
        return f'{self. type_agent}'

    class categorieMedecin(models.TextChoices):
        Infirmier = 'Infirmier'
        Medecin = 'Medecin'
        Sage_femme = 'Sage femme'
        Aide_soignant = 'Aide Soignant'
        Laboratin = 'Laboratin'
        Administratif = 'Admnistratif'

    class sexe_m(models.TextChoices):
        masculin = 'Masculin'
        feminin = 'Feminin'

    type_agent = models.fields.CharField(max_length=20, choices=categorieMedecin.choices)
    nom = models.fields.CharField(max_length=10)
    prenom = models.fields.CharField(max_length=50)
    sexe = models.fields.CharField(max_length=10, choices=sexe_m.choices)
    numero = models.fields.CharField(max_length=12, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Patient(models.Model):


    def __str__(self):
        return f'{self.prenom}'

    class sexe_m(models.TextChoices):
        masculin = 'masculin'
        feminin = 'feminin'

    class groupe(models.TextChoices):
        groupeA = 'A'
        groupeB= 'B'
        groupeAB ='AB'
        groupeO = 'O'

    class facteur(models.TextChoices):
        facteur_positif = '+'
        facteur_negatif = '-'


    nom = models.fields.CharField(max_length=20)
    prenom = models.fields.CharField(max_length=20)
    age = models.fields.IntegerField()
    sexe = models.fields.CharField(max_length=9, choices=sexe_m.choices)
    numero = models.fields.CharField(max_length=12,unique=True)
    groupe_sangin = models.fields.CharField(max_length=20, choices=groupe.choices)
    rhesus = models.fields.CharField(max_length=20, choices=facteur.choices)
    date_created = models.DateTimeField(auto_now_add=True)



class constante(models.Model):


    def __str__(self):
        return f'{self.patient}'

    poids = models.fields.IntegerField()
    temperature = models.fields.IntegerField()
    taille = models.fields.IntegerField()
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)



class consultation(models.Model):

    def __str__(self):
        return f'{self.malaise}'

    class service(models.TextChoices):
        consultation_generale = 'consultation générale'
        Urgence = 'Urgence'
        Pediatrie = 'Pediatrie'
        Radiologie ='Radiologie'
        Ecographie = 'Ecographie'
        Kinesitherapie = 'Kinesitherapie'
        Chirugie = 'Chirugie'
        Laboratoire = 'Laboratoire'
        Maternite = 'Maternite'
        Dispensaire = 'Dispensaire'
        Hospitalisation = 'Hospitalisation'
        Vaccination = 'Vaccination'
        Gynecologie = 'Gynécologie'
        Dermathologie = 'Dermathologie'


    service_consulte = models.fields.CharField(max_length=50, choices=service.choices)
    symptome_0 = models.fields.CharField(max_length=100)
    symptome_1 = models.fields.CharField(max_length=100)
    symptome_2 = models.fields.CharField(max_length=100)
    observation_0 = models.fields.CharField(max_length=100)
    observation_1 = models.fields.CharField(max_length=100)
    observation_2 = models.fields.CharField(max_length=100)
    symdrome_0 = models.fields.CharField(max_length=50)
    symdrome_1 = models.fields.CharField(max_length=50)
    symdrome_2 = models.fields.CharField(max_length=50)
    commentaire= models.fields.CharField(max_length=100)
    paraclinique_0 = models.fields.CharField(max_length=500)
    paraclinique_1 = models.fields.CharField(max_length=500)
    paraclinique_3 = models.fields.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)




class resultat(models.Model):

    def __str__(self):
        return f'{self.maladie}'

    class service(models.TextChoices):
        consultation_generale = 'consultation générale'
        Urgence = 'Urgence'
        Pediatrie = 'Pediatrie'
        Radiologie ='Radiologie'
        Ecographie = 'Ecographie'
        Kinesitherapie = 'Kinesitherapie'
        Chirugie = 'Chirugie'
        Laboratoire = 'Laboratoire'
        Maternite = 'Maternite'
        Dispensaire = 'Dispensaire'
        Hospitalisation = 'Hospitalisation'
        Vaccination = 'Vaccination'
        Gynecologie = 'Gynécologie'
        Dermathologie = 'Dermathologie'

    class pathologie(models.TextChoices):

        paludisme = 'paludisme'
        Fievre = 'Fievre'
        Diarrhe = 'Diarrhe'
        Fievre_jaune = 'Fievre jaune'
        Fievre_typhoide = 'Fievre typhoide'
        Mammographie = 'Mammographie'
        Regle_douloureuse = 'Regle_douloureuse'
        Depression = 'Depression'
        Infantille = 'Maladie infantielle'
        Audition = 'Trouble audition'


    class categorie_pathologie(models.TextChoices):

        rare = 'rare'
        tropicale = 'tropicale'
        infectieuse = 'infectieuse'
        nouvelle = 'nouvelle'
        mysterieuse = 'mysterieuse'
        mortelle = 'mortelle'



    service_consulte = models.fields.CharField(max_length=50, choices=service.choices)
    resultat_0 = models.fields.CharField(max_length=100)
    resultat_1 = models.fields.CharField(max_length=100)
    resultat_2 = models.fields.CharField(max_length=100)
    commentaire = models.fields.CharField(max_length=100)
    maladie_0 = models.fields.CharField(max_length=20, choices=pathologie.choices)
    categorie_maladie_0 = models.fields.CharField(max_length=20, choices=categorie_pathologie.choices)
    maladie_1 = models.fields.CharField(max_length=20, choices=pathologie.choices)
    categorie_maladie_1 = models.fields.CharField(max_length=20, choices=categorie_pathologie.choices)
    prescription_0 = models.fields.CharField(max_length=100)
    prescription_1 = models.fields.CharField(max_length=100)
    prescription_2 = models.fields.CharField(max_length=100)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

class pronostic(models.Model):

    def __str__(self):
        return f'{self.rechute}'

    class service(models.TextChoices):
        consultation_generale = 'consultation générale'
        Urgence = 'Urgence'
        Pediatrie = 'Pediatrie'
        Radiologie ='Radiologie'
        Ecographie = 'Ecographie'
        Kinesitherapie = 'Kinesitherapie'
        Chirugie = 'Chirugie'
        Laboratoire = 'Laboratoire'
        Maternite = 'Maternite'
        Dispensaire = 'Dispensaire'
        Hospitalisation = 'Hospitalisation'
        Vaccination = 'Vaccination'
        Gynecologie = 'Gynécologie'
        Dermathologie = 'Dermathologie'

    class valeur(models.TextChoices):
        oui = 'oui'
        non = 'non'

    serviceconsulte = models.fields.CharField(max_length=22, choices=service.choices)
    guerison = models.fields.CharField(max_length=5, choices=valeur.choices)
    rechute = models.fields.CharField(max_length=5, choices=valeur.choices)
    sequelle = models.fields.CharField(max_length=5, choices=valeur.choices)
    deces = models.fields.CharField(max_length=5, choices=valeur.choices)
    perte_de_vue = models.fields.CharField(max_length=5, choices=valeur.choices)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)



class service_anexe(models.Model):

    def __str__(self):
        return f'{self.conseil}'

    class service(models.TextChoices):

        promotion_sante = 'promotion sante'
        planification_familiale = 'planification familiale'
        service_hygiene = 'service_hygiene'

    service_consulte = models.fields.CharField(max_length=50, choices=service.choices)
    Offre = models.fields.CharField(max_length=100)
    Demande = models.fields.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)









