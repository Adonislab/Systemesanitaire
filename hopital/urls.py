from django.urls import path
from hopital.views import inscriptionPatient,\
    inscriptionConstante,inscriptionDepot,inscriptionRessourceHumaine,\
    inscriptionConsultation,inscriptionResultat,inscriptionService,\
    patient_list,patient_detail,constante_list,constante_detail,\
    consultation_list,consultation_detail,resultat_list,resultatdetail,\
    service_anexe_list,serviceannexedetail,depot_list,depotdetail,\
    inscriptionpronostic,pronostic_list,pronosticdetail,ressourcedetail,\
    ressource_list,changeressourcehumaine,changedepot,changepatient,\
    creationdonnee,visualisationdonne,modificationbase,statistique



urlpatterns = [
    path('addpatient', inscriptionPatient, name='ajoutpatient'),
    path('addobject', inscriptionDepot, name='ajoutobjet'),
    path('addhuman', inscriptionRessourceHumaine, name='ajoutressourcehumaine'),
    path('addconstance', inscriptionConstante, name='ajoutconstance'),
    path('addconsultation', inscriptionConsultation, name='ajoutconsultation'),
    path('addresultat', inscriptionResultat, name='ajoutresultat'),
    path('addconsultationannxe', inscriptionService, name='ajoutconsultationannexe'),
    path('ajoutprononstic',inscriptionpronostic , name='ajoutprononstic'),
    path('patientliste', patient_list, name='patientliste'),
    path("patientdetail/<int:id>/", patient_detail, name='patientdetail'),
    path('constancepatient/', constante_list, name='constanteliste'),
    path("constantedetail/<int:id>/", constante_detail, name ='constantedetail'),
    path('consultationliste/', consultation_list, name = 'consultationliste'),
    path("consultationdetail/<int:id>/", consultation_detail, name = 'consultationdetail'),
    path('resultatliste/', resultat_list, name ='resultatliste'),
    path("resultatdetail/<int:id>/", resultatdetail, name= 'resultatdetail'),
    path('serviceannexeliste/', service_anexe_list, name ='serviceannexeliste'),
    path("serviceannexedetail/<int:id>/", serviceannexedetail, name = 'serviceannexedetail'),
    path('depotliste/', depot_list, name ='depotliste'),
    path("depotdetail/<int:id>/", depotdetail, name ='depotdetail'),
    path('pronosticlist/', pronostic_list, name ='pronosticlist'),
    path("pronosticdetail/<int:id>/", pronosticdetail, name ='pronosticdetail'),
    path('ressourcelist/', ressource_list, name ='ressourcelist'),
    path("ressourcelistdetail//<int:id>/", ressourcedetail, name ='ressourcelistdetail'),
    path("changepatient/<int:id>/", changepatient, name ='changepatient'),
    path("changedepot/<int:id>/", changedepot, name ='changedepot'),
    path("changeresoourcehumaine/<int:id>/", changeressourcehumaine, name ='changeresoourcehumaine'),
    path('creationdonnee/', creationdonnee, name ='creationdonnee'),
    path('visualisationdonne/', visualisationdonne, name ='visualisationdonne'),
    path('modificationbase/', modificationbase, name ='modificationbase'),
    path('statistique/', statistique, name ='statistique'),
]