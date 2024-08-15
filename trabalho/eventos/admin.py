from django.contrib import admin
from .models import EventoCultural

class EventoCulturalAdmin(admin.ModelAdmin):
    list_display = ('evento', 'data_evento', 'entrada', 'horário', 'local', 'quantidade_de_ingressos')
    search_fields = ('evento', 'local', 'entrada')
    list_filter = ('evento', 'local', 'entrada')

admin.site.register(EventoCultural, EventoCulturalAdmin)