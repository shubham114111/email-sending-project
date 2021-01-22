from django import forms

class Send(forms.Form):
    email = forms.EmailField()
