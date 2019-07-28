from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Datos


class DataForm(forms.ModelForm):

    class Meta:
        model = Datos
        fields = "__all__"

        labels = {
            'P_accu': _('Lluvias acumuladas [mms]'),
            "T_avg_prev": _("Temperatura promedio un mes previo a la cosecha [C]"),
            "Rad_accu_prev1": _("Radiación acumulada un mes previo a la cosecha [µmol·m²s-1]"),
        }
