from django.contrib import admin

from .models import Eintrag

class EintragAdmin(admin.ModelAdmin):
    list_display = ('User','Name','Anmeldung','Email','pub_date')
admin.site.register(Eintrag, EintragAdmin)