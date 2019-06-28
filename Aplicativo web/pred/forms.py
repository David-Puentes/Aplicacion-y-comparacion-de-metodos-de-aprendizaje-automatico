from django import forms

from .models import Datos


class DataForm(forms.ModelForm):

    class Meta:
        model = Datos
        fields = "__all__"
