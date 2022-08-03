from django import forms
from .models import LikeLion

class LikeLionCreateForm(forms.ModelForm):
    class Meta:
        model = LikeLion
        #fields = ["name","part","age","bio",]
        fields = "__all__"

    
    
