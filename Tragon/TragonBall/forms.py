from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30, required=True)
    correo = forms.EmailField(label="Correo", required=True)
    mensaje = forms.CharField(label="Mensaje", max_length=1000, widget=forms.Textarea, required=True)