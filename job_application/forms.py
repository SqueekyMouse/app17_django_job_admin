from django import forms

# manually created form class to get data from index form!!
class ApplicationForm(forms.Form):
    first_name=forms.CharField(max_length=80)
    last_name=forms.CharField(max_length=80)
    email=forms.EmailField()
    date=forms.DateField()
    occupation=forms.CharField(max_length=80)