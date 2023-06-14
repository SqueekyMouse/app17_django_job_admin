from django.shortcuts import render
from .forms import ApplicationForm # import form class we created

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
            print(first_name)
    return(render(request,template_name='index.html')) 

