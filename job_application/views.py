from django.shortcuts import render
from .forms import ApplicationForm # import form class we created
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
# html need to be in templated folder unless 
# scpecified in settings.py templates section!!

def index(request):
    if request.method=='POST':
        form=ApplicationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            date=form.cleaned_data['date']
            occupation=form.cleaned_data['occupation']
            # print(first_name)
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            messages.success(request,'Form submitted successfully!')

            message_body=f'Anew job application was submitted. Thank you, {first_name}'
            email_message=EmailMessage('Form submission confirmation', message_body, to=[email])
            email_message.send()


    return(render(request,template_name='index.html')) 

