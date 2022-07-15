from django.contrib import admin
from authentification.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('role', 'nom_du_centre', 'numero_telephone')


admin.site.register(User,UserAdmin)
