from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(required = True, max_length = 60)

