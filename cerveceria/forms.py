import django
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
    correo_electrónico = forms.EmailField()
    asunto = forms.CharField(max_length = 70)
    mensaje = forms.CharField(widget = forms.Textarea(attrs = {'class':'text-area-no-resize'}))