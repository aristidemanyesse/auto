from .models import Agence, Employe
from django.forms import ModelForm

# Create your models here.


class AgenceForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Agence



class EmployeForm(ModelForm):
    class Meta:
        fields = ["agence", "first_name", "last_name", "email", "contact", "adresse", "image"]
        model = Employe

