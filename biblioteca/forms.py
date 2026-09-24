from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        # fields = ['isbn', 'titulo']
        fields = '__all__'
        
        widgets={
            'isbn': forms.TextInput(attrs={
                'placeholder': 'Ej: 907-0123458948'
            }),
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ingrese aqui el titulo del libro'
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'type':'date',
            })
            
            
        }