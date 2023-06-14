from django.shortcuts import render

# Create your views here.
def index(request):
    return(render(request,template_name='index.html')) 

# html need to be in templated folder unless 
# scpecified in settings.py templates section!!