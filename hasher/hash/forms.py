from django import forms


class HashForm(forms.Form):
    name = forms.CharField(
        max_length=200, label="Enter here", widget=forms.TextInput(attrs={'class': 'font-control'}))
