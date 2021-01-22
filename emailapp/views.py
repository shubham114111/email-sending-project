from django.shortcuts import render
from . import forms

def send(request):
    obj = forms.Send()
    return render(request, 'emailapp/index.html', {'form':obj})