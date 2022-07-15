from django import forms
from hopital.models import Depot,RessourceHumaine,Patient,constante,resultat,service_anexe,consultation,pronostic


class formdepot(forms.ModelForm):
    class Meta:
        model = Depot
        fields = '__all__'


class formressourceHumaine(forms.ModelForm):
    class Meta:
        model = RessourceHumaine
        fields = '__all__'


class formPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class formconstante(forms.ModelForm):
    class Meta:
        model = constante
        fields = '__all__'

class formconsultation(forms.ModelForm):
    class Meta:
        model = consultation
        fields = '__all__'

class formresultat(forms.ModelForm):
    class Meta:
        model = resultat
        fields = '__all__'

class formpronostic(forms.ModelForm):
    class Meta:
        model = pronostic
        fields = '__all__'



class formservice_anexe(forms.ModelForm):
    class Meta:
        model = service_anexe
        fields = '__all__'