from django import forms

class UserForm(forms.Form):
    conteudo = forms.CharField(max_lenght=200)
    observacao = forms.CharField(max_lenght=200)