from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
