from django import forms
from .models import Pet

class PetForm(forms.ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome.upper() == 'PUTINHO':
            raise forms.ValidationError('Nome muito ofensivo')
        return nome
    
    class Meta:
        model = Pet
        fields = '__all__'