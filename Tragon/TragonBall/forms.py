from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="nombre", max_length=30, required=True)
    correo = forms.EmailField(label="correo", required=True)
    mensaje = forms.CharField(label="mensaje", max_length=1000, widget=forms.Textarea, required=True)