from django import forms
from ToDo_app.models import List

class NewListForm(forms.ModelForm):
    class Meta:
        model = List
        fields ='__all__'
