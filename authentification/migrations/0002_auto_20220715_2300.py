# Generated by Django 4.0.6 on 2022-07-15 23:00

from django.db import migrations


def create_groups(apps, schema_migration):
    User = apps.get_model('authentification', 'User')
    Group = apps.get_model('auth', 'Group')

    # RELAIS_COMMUNAUTAIRE = apps.get_model('authentification', 'User')
    # CENTRE_DE_SANTE_ARRONDISSEMENT = apps.get_model('authentification', 'User')
    # CENTRE_DE_SANTE_COMMUNAL = apps.get_model('authentification', 'User')
    # HOPITAL_DE_ZONE = apps.get_model('authentification', 'User')
    # HOPITAL_DE_ZONE_DEPARTEMENTAL = apps.get_model('authentification', 'User')
    # HOPITAL_NATIONAL = apps.get_model('authentification', 'User')
    # HOPITAL_PRIVE = apps.get_model('authentification', 'User')
    # MINISTERE_DE_LA_SANTE = apps.get_model('authentification', 'User')
    # DOCTEUR = apps.get_model('authentification', 'User')
    # AIDE_SOIGNANT = apps.get_model('authentification', 'User')
    # ADMINISTRATIF_HOPITAL = apps.get_model('authentification', 'User')
    Permission = apps.get_model('auth', 'Permission')

    add_Depot = Permission.objects.get(codename='add_Depot')
    change_Depot = Permission.objects.get(codename='change_Depot')
    view_Depot = Permission.objects.get(codename='view_Depot')

    add_RessourceHumaine = Permission.objects.get(codename='add_RessourceHumaine')
    change_RessourceHumaine = Permission.objects.get(codename='change_RessourceHumaine')
    view_RessourceHumaine = Permission.objects.get(codename='view_RessourceHumaine')

    add_Patient = Permission.objects.get(codename='add_Patient')
    change_Patient = Permission.objects.get(codename='change_Patient')
    view_Patient = Permission.objects.get(codename='view_Patient')

    add_constante = Permission.objects.get(codename='add_constante')
    view_constante = Permission.objects.get(codename='view_constante')

    add_consultation = Permission.objects.get(codename='add_consultation')
    view_consultation = Permission.objects.get(codename='view_consultation')

    add_resultat = Permission.objects.get(codename='add_resultat')
    view_resultat = Permission.objects.get(codename='view_resultat')

    add_pronostic = Permission.objects.get(codename='add_pronostic')
    view_pronostic = Permission.objects.get(codename='view_pronostic')

    add_service_anexe = Permission.objects.get(codename='add_service_anexe')
    view_service_anexe = Permission.objects.get(codename='view_service_anexe')

    creator_administration = [
        add_Patient,
        add_Depot,
        change_Depot,
        view_Depot,
        add_RessourceHumaine,
        change_RessourceHumaine,
        view_RessourceHumaine,
    ]

    centre = [
        view_RessourceHumaine,
        add_Patient,
        view_Patient,
        view_constante,
        view_consultation,
        view_resultat,
        view_service_anexe,
        view_pronostic,
    ]

    creator_permissions = [
        add_Depot,
        view_Depot,
        add_RessourceHumaine,
        change_RessourceHumaine,
        view_RessourceHumaine,
        add_Patient,
        view_Patient,
        view_constante,
        view_consultation,
        view_resultat,
        view_service_anexe,
        view_pronostic,
    ]

    docteur_permission = [
        add_Patient,
        change_Patient,
        view_Patient,
        view_constante,
        add_consultation,
        view_consultation,
        add_resultat,
        view_resultat,
        add_service_anexe,
        view_service_anexe,
        add_pronostic,
        view_pronostic,
    ]

    aide_permissions = [
        add_Patient,
        view_Patient,
        add_constante,
    ]

    hopitaladministation = [
        add_Patient,
        change_Patient,
        view_Patient,
        add_Depot,
        change_Depot,
        view_Depot,
        add_RessourceHumaine,
        change_RessourceHumaine,
        view_RessourceHumaine,
    ]

    RELAIS_COMMUNAUTAIRE = Group(name='RELAIS_COMMUNAUTAIRE')
    RELAIS_COMMUNAUTAIRE.save()
    RELAIS_COMMUNAUTAIRE.permissions.add(centre)
    RELAIS_COMMUNAUTAIRE.permissions.set(centre)

    CENTRE_DE_SANTE_ARRONDISSEMENT = Group(name='CENTRE_DE_SANTE_ARRONDISSEMENT')
    CENTRE_DE_SANTE_ARRONDISSEMENT.save()
    CENTRE_DE_SANTE_ARRONDISSEMENT.permissions.add(centre)
    CENTRE_DE_SANTE_ARRONDISSEMENT.permissions.set(centre)

    CENTRE_DE_SANTE_COMMUNAL = Group(name='CENTRE_DE_SANTE_COMMUNAL')
    CENTRE_DE_SANTE_COMMUNAL.save()
    CENTRE_DE_SANTE_COMMUNAL.permissions.add(creator_administration)
    CENTRE_DE_SANTE_COMMUNAL.permissions.set(creator_administration)

    HOPITAL_DE_ZONE = Group(name='HOPITAL_DE_ZONE')
    HOPITAL_DE_ZONE.save()
    HOPITAL_DE_ZONE.permissions.add(creator_administration)
    HOPITAL_DE_ZONE.permissions.set(creator_administration)

    HOPITAL_DE_ZONE_DEPARTEMENTAL = Group(name='HOPITAL_DE_ZONE_DEPARTEMENTAL')
    HOPITAL_DE_ZONE_DEPARTEMENTAL.save()
    HOPITAL_DE_ZONE_DEPARTEMENTAL.permissions.add(creator_administration)
    HOPITAL_DE_ZONE_DEPARTEMENTAL.permissions.set(creator_administration)

    HOPITAL_NATIONAL = Group(name='HOPITAL_NATIONAL')
    HOPITAL_NATIONAL.save()
    HOPITAL_NATIONAL.permissions.add(creator_permissions)
    HOPITAL_NATIONAL.permissions.set(creator_permissions)

    HOPITAL_PRIVE = Group(name='HOPITAL_PRIVE')
    HOPITAL_PRIVE.save()
    HOPITAL_PRIVE.permissions.add(creator_permissions)
    HOPITAL_PRIVE.permissions.set(creator_permissions)

    MINISTERE_DE_LA_SANTE = Group(name='MINISTERE_DE_LA_SANTE')
    MINISTERE_DE_LA_SANTE.save()
    MINISTERE_DE_LA_SANTE.permissions.add(creator_permissions)
    MINISTERE_DE_LA_SANTE.permissions.set(creator_permissions)

    DOCTEUR = Group(name='DOCTEUR')
    DOCTEUR.save()
    DOCTEUR.permissions.add(docteur_permission)
    DOCTEUR.permissions.set(docteur_permission)

    AIDE_SOIGNANT = Group(name='AIDE_SOIGNANT')
    AIDE_SOIGNANT.save()
    AIDE_SOIGNANT.add(aide_permissions)
    AIDE_SOIGNANT.set(aide_permissions)

    ADMINISTRATIF_HOPITAL = Group(name='ADMINISTRATIF_HOPITAL')
    ADMINISTRATIF_HOPITAL.save()
    ADMINISTRATIF_HOPITAL.add(hopitaladministation)
    ADMINISTRATIF_HOPITAL.set(hopitaladministation)


    for user in User.objects.all():
        if user.role == 'RELAIS_COMMUNAUTAIRE':
            RELAIS_COMMUNAUTAIRE.user_set.add(user)
        if user.role == 'CENTRE_DE_SANTE_ARRONDISSEMENT':
            CENTRE_DE_SANTE_ARRONDISSEMENT.user_set.add(user)
        if user.role == 'CENTRE_DE_SANTE_COMMUNAL':
            CENTRE_DE_SANTE_COMMUNAL.user_set.add(user)
        if user.role == 'HOPITAL_DE_ZONE':
            HOPITAL_DE_ZONE.user_set.add(user)
        if user.role == 'HOPITAL_DE_ZONE_DEPARTEMENTAL':
            HOPITAL_DE_ZONE_DEPARTEMENTAL.user_set.add(user)
        if user.role == 'HOPITAL_NATIONAL':
            HOPITAL_NATIONAL.user_set.add(user)
        if user.role == 'HOPITAL_PRIVE':
            HOPITAL_PRIVE.user_set.add(user)
        if user.role == 'MINISTERE_DE_LA_SANTE':
            MINISTERE_DE_LA_SANTE.user_set.add(user)
        if user.role == 'DOCTEUR':
            DOCTEUR.user_set.add(user)
        if user.role == 'AIDE_SOIGNANT':
            AIDE_SOIGNANT.user_set.add(user)
        if user.role == 'ADMINISTRATIF_HOPITAL':
            ADMINISTRATIF_HOPITAL.user_set.add(user)

class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
    ]