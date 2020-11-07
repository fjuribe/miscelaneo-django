from django import forms

class ContactoForm(forms.Form):
	yourname=forms.CharField(max_length=100,label='tu nombre')
	email=forms.EmailField(required=False,label='Tu correo')
	subject=forms.CharField(max_length=100)
	message=forms.CharField(widget=forms.Textarea)