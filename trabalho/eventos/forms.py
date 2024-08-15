from django import forms
from .models import EventoCultural

class EventoCulturalForm(forms.ModelForm):
    class Meta:
        model = EventoCultural
        fields = ['evento', 'data_evento', 'entrada', 'horário', 'local','entrada', 'quantidade_de_ingressos']
        widgets = {
            'data_evento': forms.DateInput(attrs={'type': 'date'}),
            'horário': forms.TimeInput(attrs={'type': 'time'}),
            'local': forms.Select(attrs={'class': 'custom-select'}),
            'entrada': forms.Select(attrs={'class': 'custom-select'}),
            'evento': forms.Select(attrs={'class': 'custom-select'}),
            'entrada': forms.RadioSelect(attrs={'class': 'custom-select'}),
        }
