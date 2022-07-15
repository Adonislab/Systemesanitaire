from django.contrib import admin

from hopital.models import Depot,RessourceHumaine,\
    Patient,constante,consultation,resultat,service_anexe,pronostic

class DepotAdmin(admin.ModelAdmin):
    list_display = ('type_du_produit', 'nom_du_produit', 'nombre_de_stoke')

class RessourceHumaineAdmin(admin.ModelAdmin):
    list_display = ('type_agent', 'prenom', 'numero')


class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'sexe')

class ConstanteAdmin(admin.ModelAdmin):
    list_display = ('patient', 'poids', 'temperature')

class consultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'symptome_0', 'observation_0')

class resultatAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service_consulte', 'maladie_0')

class pronosticAdmin(admin.ModelAdmin):
    list_display = ('patient','serviceconsulte', 'guerison')


class service_anexeAdmin(admin.ModelAdmin):
    list_display = ('Offre', 'service_consulte', 'Demande')



admin.site.register(Depot, DepotAdmin)
admin.site.register(RessourceHumaine, RessourceHumaineAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(constante, ConstanteAdmin)
admin.site.register(consultation, consultationAdmin)
admin.site.register(resultat, resultatAdmin)
admin.site.register(service_anexe, service_anexeAdmin)
admin.site.register(pronostic, pronosticAdmin)
