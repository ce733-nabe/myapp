from django import forms

class IdKensaku(forms.Form):
    id = forms.IntegerField(label = "ID")