from django import forms
import re





def check_name(value):
    if value[0].lower()=='z':
        raise forms.ValidationError('name shoud contain only alphabets')


class RigistrationForm(forms.Form):
    name=forms.CharField(max_length=20,validators=[check_name])
    MBno=forms.IntegerField()
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput)