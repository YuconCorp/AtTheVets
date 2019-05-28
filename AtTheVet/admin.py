from django.contrib import admin

# Register your models here.
from .models import Factuur
from .models import Declaratie

# fancyfy the Factuur and Declaratie view


class FactuurAdmin(admin.ModelAdmin):
    list_display = ["factuur_id", "factuur_datum", "factuur_bedrag"]

    class Meta:
        model = Factuur


class DeclaratieAdmin(admin.ModelAdmin):
    list_display = ["declaratie_id", "declaratie_gedeclareerd", "declaratie_retour"]

    class Meta:
        model = Declaratie


admin.site.register(Factuur, FactuurAdmin)
admin.site.register(Declaratie, DeclaratieAdmin)
