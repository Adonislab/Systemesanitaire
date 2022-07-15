from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from hopital.forms import formdepot,formressourceHumaine,\
    formPatient,formconstante,formresultat,formservice_anexe,formconsultation,formpronostic

from hopital.models import Depot,RessourceHumaine,\
    Patient,constante,resultat,service_anexe,consultation,pronostic


import seaborn as sns
import pandas as pd

@login_required
def home(request):
    return render(request, 'hopital/home.html')

@login_required
def creationdonnee(request):
    return render(request, 'hopital/creation/creationdata.html')

@login_required
@permission_required('hopital.view_Patient', raise_exception=True)
@permission_required('hopital.view_pronostic', raise_exception=True)
def visualisationdonne(request):

    patient = Patient.objects.all()

    constance = constante.objects.all()
    resulta = resultat.objects.all()
    prono = pronostic.objects.all()


    return render(request,
                  'hopital/statistique/visualisationstatistique.html',
                  {'patient': len(patient)}
                  )

@login_required
def modificationbase(request):
    return render(request, 'hopital/changement/modicationbase.html')


@login_required
@permission_required('hopital.view_Patient', raise_exception=True)
@permission_required('hopital.view_pronostic', raise_exception=True)
def statistique(request):
    return render(request, 'hopital/lecture_traitement/visualisationDataOfpatient.html')




@login_required
@permission_required('hopital.add_Depot', raise_exception=True)
def inscriptionDepot(request):
    if request.method == 'POST':
        form = formdepot(request.POST)
        if form.is_valid():
            depot = form.save()
            return redirect('depotdetail',depot.id)
    else:
        form = formdepot()
    return render(request,
                  'hopital/creation/inscriptionDepot.html',
                  {'form' : form})

@login_required
@permission_required('hopital.view_Depot', raise_exception=True)
def depot_list(request):
    depot_li = Depot.objects.all()
    return render(request,
                      'hopital/lecture_traitement/VueDepotListe.html',
                      {'Depot': depot_li})
@login_required
@permission_required('hopital.view_Depot', raise_exception=True)
def depotdetail(request,id):
    depot_det = Depot.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VueDepotDetaille.html',
                  {'depot': depot_det})

@login_required
@permission_required('hopital.change_Depot', raise_exception=True)
def changedepot(request, id):
    depot_change = Depot.objects.get(id=id)

    if request.method == 'POST':
        form = formdepot(request.POST,instance=depot_change)

        if form.is_valid():
            form.save()

            return redirect('depotdetail', depot_change.id)

    else:
        form = formdepot(instance = depot_change)


    return render(request,
                  'hopital/changement/ChangementDepot.html',
                  {'depot': form})


@login_required
@permission_required('hopital.add_RessourceHumaine', raise_exception=True)
def inscriptionRessourceHumaine(request):

    if request.method == 'POST':
        form = formressourceHumaine(request.POST)
        if form.is_valid():

            ressource = form.save()

            return redirect('ressourcelistdetail',ressource.id)

    else:
        form = formressourceHumaine()

    return render(request,
                  'hopital/creation/inscriptionRessourceHumaine.html',
                  {'form': form})


@login_required
@permission_required('hopital.view_RessourceHumaine', raise_exception=True)
def ressource_list(request):
    ressource_li = RessourceHumaine.objects.all()
    return render(request,
                      'hopital/lecture_traitement/VueRessourceHumaineListe.html',
                      {'ressource': ressource_li})


@login_required
@permission_required('hopital.view_RessourceHumaine', raise_exception=True)
def ressourcedetail(request,id):
    RessourceHumaine_det = RessourceHumaine.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VueRessourceHumaineDetaille.html',
                  {'ressource': RessourceHumaine_det})


@login_required
@permission_required('hopital.view_RessourceHumaine', raise_exception=True)
@permission_required('hopital.change_RessourceHumaine', raise_exception=True)
def changeressourcehumaine(request, id):
    ressourehumaine_change = RessourceHumaine.objects.get(id=id)

    if request.method == 'POST':
        form = formressourceHumaine(request.POST,instance = ressourehumaine_change)
        if form.is_valid():
            form.save()
            return redirect('resultatdetail', ressourehumaine_change.id)

    else:
        form = formressourceHumaine(instance = ressourehumaine_change)



    return render(request,
                  'hopital/changement/ChangementRessourceHmaine.html',
                  {'ressourcehumaine': form})


@login_required
@permission_required('hopital.add_Patient', raise_exception=True)
def inscriptionPatient(request):

    if request.method == 'POST':
        form_patient = formPatient(request.POST)
        if form_patient.is_valid():

            patient = form_patient.save()

            return redirect('patientdetail',patient.id)

    else:
        form_patient = formPatient()

    return render(request,
                  'hopital/creation/inscriptionPatient.html',
                  {'form': form_patient})

@login_required
@permission_required('hopital.view_Patient', raise_exception=True)
def patient_list(request):
   patient = Patient.objects.all()
   return render(request,
           'hopital/lecture_traitement/VuePatientListe.html',
           {'patient': patient})

@login_required
@permission_required('hopital.view_Patient', raise_exception=True)
def patient_detail(request, id):
    detail_patient = Patient.objects.get(id=id)
    return render(request,
          'hopital/lecture_traitement/VuePatientDetaille.html',
         {'patient': detail_patient})

@login_required
@permission_required('hopital.view_Patient', raise_exception=True)
@permission_required('hopital.change_Patient', raise_exception=True)
def changepatient(request, id):
    patient_change = Patient.objects.get(id=id)

    if request.method == 'POST':
        form = formPatient(request.POST,instance=patient_change)
        if form.is_valid():
            form.save()
            return redirect('patientdetail', patient_change.id)
    else:
        form = formPatient(instance=patient_change)



    return render(request,
                  'hopital/changement/ChangementInscriptionPatient.html',
                  {'patient': form})

@login_required
@permission_required('hopital.add_constante', raise_exception=True)
def inscriptionConstante(request):

    if request.method == 'POST':
        form = formconstante(request.POST)
        if form.is_valid():

            constance = form.save()

            return redirect('constantedetail',constance.id)

    else:
        form = formconstante()

    return render(request,
                  'hopital/creation/inscriptionConstante.html',
                  {'form': form})


@login_required
@permission_required('hopital.view_constante', raise_exception=True)
def constante_list(request):
   constance = constante.objects.all()
   return render(request,
           'hopital/lecture_traitement/VueConstanteListe.html',
           {'constance': constance})

@login_required
@permission_required('hopital.view_constante', raise_exception=True)
def constante_detail(request, id):
    constance = constante.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VueConstanteDetaille.html',
                  {'constance': constance})

@login_required
@permission_required('hopital.add_consultation', raise_exception=True)
def inscriptionConsultation(request):

    if request.method == 'POST':
        form = formconsultation(request.POST)
        if form.is_valid():

            consultation = form.save()

            return redirect('consultationdetail',consultation.id)

    else:
        form = formconsultation()

    return render(request,
                  'hopital/creation/inscriptionConsultation.html',
                  {'form': form})

@login_required
@permission_required('hopital.view_consultation', raise_exception=True)
def consultation_list(request):
   consultation_li = consultation.objects.all()
   return render(request,
           'hopital/lecture_traitement/VueConsultationListe.html',
           {'consultation': consultation_li})


@login_required
@permission_required('hopital.view_consultation', raise_exception=True)
def consultation_detail(request, id):
  consultation_det = consultation.objects.get(id=id)
  return render(request,
          'hopital/lecture_traitement/VueConsultationDetaille.html',
          {'consultation': consultation_det})


@login_required
@permission_required('hopital.add_resultat', raise_exception=True)
def inscriptionResultat(request):

    if request.method == 'POST':
        form = formresultat(request.POST)
        if form.is_valid():

            resultat = form.save()

            return redirect('resultatdetail',resultat.id)

    else:
        form = formresultat()

    return render(request,
                  'hopital/creation/inscriptionResultat.html',
                  {'form': form})

@login_required
@permission_required('hopital.view_resultat', raise_exception=True)
def resultat_list(request):
   resultat_li = resultat.objects.all()
   return render(request,
           'hopital/lecture_traitement/VueResultatListe.html',
           {'resultat': resultat_li})

@login_required
@permission_required('hopital.view_resultat', raise_exception=True)
def resultatdetail(request, id):
    resultat_det = resultat.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VueResultatDetaille.html',
                  {'resultat': resultat_det})

@login_required
@permission_required('hopital.add_service_anexe', raise_exception=True)
def inscriptionService(request):

    if request.method == 'POST':
        form = formservice_anexe()
        if form.is_valid():

            service_anexe = form.save()

            return redirect("serviceannexedetail",service_anexe.id)

    else:
        form = formservice_anexe()

    return render(request,
                  'hopital/creation/inscriptionServiceAnnexe.html',
                  {'form': form})


@login_required
@permission_required('hopital.view_service_anexe', raise_exception=True)
def service_anexe_list(request):
   service_li = service_anexe.objects.all()
   return render(request,
           'hopital/lecture_traitement/VueServiceannexeListe.html',
           {'service_anexe': service_li})

@login_required
@permission_required('hopital.view_service_anexe', raise_exception=True)
def serviceannexedetail(request,id):
    service_annexe = service_anexe.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VueServiceannexeDetaille.html',
                  {'service_anexe': service_annexe})

@login_required
@permission_required('hopital.add_pronosticanexe', raise_exception=True)
def inscriptionpronostic(request):

    if request.method == 'POST':
        form = formpronostic(request.POST)
        if form.is_valid():

            prono =form.save()

            return redirect("pronosticdetail",prono.id)

    else:
            form = formpronostic()


    return render(request,
                  'hopital/creation/inscriptionPronostic.html',
                  {'form': form})

@login_required
@permission_required('hopital.view_pronosticanexe', raise_exception=True)
def pronostic_list(request):
   pronostic_li = service_anexe.objects.all()
   return render(request,
           'hopital/lecture_traitement/VuePronosticListe.html',
           {'prono': pronostic_li})


@login_required
@permission_required('hopital.view_pronosticanexe', raise_exception=True)
def pronosticdetail(request,id):
    pronostic_det = pronostic.objects.get(id=id)
    return render(request,
                  'hopital/lecture_traitement/VuePronosticDetaille.html',
                  {'prono': pronostic_det})