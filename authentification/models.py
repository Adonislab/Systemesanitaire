from django.db import models
from django.contrib.auth.models import AbstractUser,Group


class User(AbstractUser):

    def __str__(self):
        return f'{self.nom_du_centre}'

    RELAIS_COMMUNAUTAIRE_CHEF_POSTE = 'Relais communautaire (Chef poste)'
    CENTRE_DE_SANTE_ARRONDISSEMENT_CHEF_POSTE = "Centre de santé d'arrondissment (Chef poste)"
    CENTRE_DE_SANTE_COMMUNAL_MEDECIN_CHEF = "Centre de santé de commune (Medecin Chef)"
    HOPITAL_DE_ZONE_COORDONATEUR_ZONE = "Hopital de zone (Coordonnateur de Zone)"
    HOPITAL_DE_ZONE_DEPARTEMENTAL_COORDONATEUR = "Hopital de zone départemental (Coordonnateur de Zone départementale)"
    HOPITAL_NATIONAL_DIRECTEUR = "Hopital national (Directeur)"
    HOPITAL_PRIVE_DIRECTEUR = "Hopital privé (Directeur)"
    MINISTERE_DE_LA_SANTE = "Ministère de la santé"
    MEDECIN = 'Medecin'
    AIDE_SOIGNANT = 'Aide soignant'
    ADMINISTRATIF_HOPITAL = "Administratif d'un centre"

    ROLE_CHOICES = (
        (RELAIS_COMMUNAUTAIRE_CHEF_POSTE, 'Relais communautaire (Chef poste)'),
        (CENTRE_DE_SANTE_ARRONDISSEMENT_CHEF_POSTE, "Centre de santé d'arrondissment (Chef poste)"),
        (CENTRE_DE_SANTE_COMMUNAL_MEDECIN_CHEF, "Centre de santé de commune (Medecin Chef)"),
        (HOPITAL_DE_ZONE_COORDONATEUR_ZONE, "Hopital de zone (Coordonnateur de Zone)"),
        (HOPITAL_DE_ZONE_DEPARTEMENTAL_COORDONATEUR, "Hopital de zone départemental (Directeur)"),
        (HOPITAL_NATIONAL_DIRECTEUR, "Hopital national (Directeur)"),
        (HOPITAL_PRIVE_DIRECTEUR, "Hopital privé (Directeur)"),
        (MINISTERE_DE_LA_SANTE, "Ministère de la santé"),
        (MEDECIN, 'Medecin'),
        (AIDE_SOIGNANT, 'Aide soignant'),
        (ADMINISTRATIF_HOPITAL, "Administratif d'un centre") ,
    )

    role = models.CharField(max_length=70, choices = ROLE_CHOICES, verbose_name='Rôle')
    departement = models.CharField(max_length=30)
    commune = models.CharField(max_length=30)
    arrondissement = models.CharField(max_length=30)
    nom_du_centre = models.CharField(unique=True,max_length=30)
    numero_telephone = models.CharField(unique=True,max_length=30)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.RELAIS_COMMUNAUTAIRE_CHEF_POSTE:
            group = Group.objects.get(name='RELAIS_COMMUNAUTAIRE_CHEF_POSTE')
            group.user_set.add(self)
        elif self.role == self.CENTRE_DE_SANTE_ARRONDISSEMENT_CHEF_POSTE:
            group = Group.objects.get(name='CENTRE_DE_SANTE_ARRONDISSEMENT_CHEF_POSTE')
            group.user_set.add(self)
        elif self.role == self.CENTRE_DE_SANTE_COMMUNAL_MEDECIN_CHEF:
            group = Group.objects.get(name='CENTRE_DE_SANTE_COMMUNAL_MEDECIN_CHEF')
            group.user_set.add(self)
        elif self.role == self.HOPITAL_DE_ZONE_COORDONATEUR_ZONE:
            group = Group.objects.get(name='HOPITAL_DE_ZONE_COORDONATEUR_ZONE')
            group.user_set.add(self)
        elif self.role == self.HOPITAL_NATIONAL_DIRECTEUR:
            group = Group.objects.get(name='HOPITAL_NATIONAL_DIRECTEUR')
            group.user_set.add(self)
        elif self.role == self.HOPITAL_PRIVE_DIRECTEUR:
            group = Group.objects.get(name='HOPITAL_PRIVE_DIRECTEUR')
            group.user_set.add(self)
        elif self.role == self.MINISTERE_DE_LA_SANTE:
            group = Group.objects.get(name='MINISTERE_DE_LA_SANTE')
            group.user_set.add(self)
        elif self.role == self.MEDECIN:
            group = Group.objects.get(name='MEDECIN')
            group.user_set.add(self)
        elif self.role == self.AIDE_SOIGNANT:
            group = Group.objects.get(name='AIDE_SOIGNANT')
            group.user_set.add(self)
        elif self.role == self.ADMINISTRATIF_HOPITAL:
            group = Group.objects.get(name='ADMINISTRATIF_HOPITAL')
            group.user_set.add(self)


