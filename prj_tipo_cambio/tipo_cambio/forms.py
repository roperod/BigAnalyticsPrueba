from django import forms

from .models import TipoDeCambio

class CDateInput(forms.DateInput):
    input_type = 'date'

class TipoDeCambioForm(forms.ModelForm):
    class Meta:
        model = TipoDeCambio
        fields = ['venta', 'compra', 'fecha']
        widgets = {
            'fecha': CDateInput(attrs={
                'class': 'form-date'
            }),
            'compra': forms.HiddenInput(),
            'venta': forms.HiddenInput()
        }