from django import forms
from .models import Publisher,Author,Book

class PublisherForm(forms.Modelform):
    class Meta:
        model=Publisherfeilds = ['name','address','city','country']
        widgets = { 
            'address':forms.Textarea(attrs= {'row':3})
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','last_name','email']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ['title','isb','published_date','publisher','authors']
        widgets = {
            'published_date': forms.DateInput(attrs={'type':'date'}),
            'authors': forms.CheckboxSelectMultiple(),
        }
        