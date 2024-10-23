from django import forms
from .models import Student

class Details(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name', 'age', 'phone', 'address', 'skills']
    
