from django.contrib import admin

from .models import Eintrag

class EintragAdmin(admin.ModelAdmin):
    list_display = ('Name','Anmeldung', 'Essen','Email','pub_date')
admin.site.register(Eintrag, EintragAdmin)