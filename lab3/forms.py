from django import forms
from .models import books
#from django .db import filter
class booksForm(forms.ModelForm):

    class Meta:
        model = books
        fields  = "__all__"
    
#class edd(forms.ModelForm):
#   class Meta:
#      model = books
#     fields  = "__all__"