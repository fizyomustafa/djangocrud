from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"img": "Resim", "first_name": "Adınız", "last_name":"Soyadınız", "number":"Numaranız"}