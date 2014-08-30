from django import forms
from allModel.models import SuUserDepartment 

class addDept(forms.ModelForm):
    class Meta:
        model=SuUserDepartment