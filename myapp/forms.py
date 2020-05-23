from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=39, min_length=5)
    password = forms.CharField(max_length=128, min_length=8)

class SigninForm(forms.Form):
    username = forms.CharField(max_length=39, min_length=5)
    password = forms.CharField(max_length=128, min_length=8)