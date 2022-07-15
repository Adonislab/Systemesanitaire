import seaborn as sns
import pandas as pd
from hopital.models import Patient,constante,resultat,consultation,pronostic

def graph():
    # variable d
    patient = Patient.objects.all()
    # hist_age = sns.distplot(age_patient, kde=False)
    constance = constante.objects.all()
    resulta = resultat.objects.all()
    prono = pronostic.objects.all()
    # variable de barplot sexe
    # cambert_sexe = sns.countplot(x= sexe_patient , data = len(Patient.objects.all()) )

    # variable de barplot maladie
    deces = pronostic.objects.all().deces
    maladie_0 = resultat.objects.all().maladie_0
    maladie = sns.countplot(x=maladie_0, data=len(resultat.objects.all()))
    # variable indice
    poids_patient = constante.objects.all().poids
    poids_temperature = constante.objects.all().taille
    indice_cor = sns.distplot(poids_patient / poids_temperature, bins=[18.5, 25, 30, 35, 40],
                              norm_hist=True, kde=False, labels=['poids normal',
                                                                 'surpoids', 'obésité modérée',
                                                                 'obésité sévère'])
    # variable sexe vs maladie
    tips = pd.merge(resultat.objects.all(), Patient.objects.all())
    tips_1 = pd.merge(pronostic.objects.all(), Patient.objects.all())
    maladie_sexe = sns.catplot(x=maladie_0, y=sexe_patient, data=tips)
    maladie_age = sns.catplot(x=maladie_0, y=age_patient, data=tips_1)
    deces = sns.barplot(x=deces, labels=deces)
    deces_age = sns.catplot(x=deces, y=age_patient, data=tips)

    context = {'patient': patient,
               'constance': constance,
               'resultat': resulta,
               'pronostic': resulta}
