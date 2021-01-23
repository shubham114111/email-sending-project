from django.shortcuts import render
from . import forms
from emailproject.settings import EMAIL_HOST_USER

from django.core.mail import send_mail

def send(request):
    obj = forms.Send()
    if request.method == 'POST':
        obj=forms.Send(request.POST)
        subject = 'An email from Django'
        message = 'This is sending from django'
        recepient = str(obj['email'].value()) 
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'emailapp/success.html', {'recepient': recepient})

    return render(request, 'emailapp/index.html', {'form':obj})