from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from first.models import fooditem



class MenuForm(forms.ModelForm):

    class Meta():
        model=fooditem
        fields='__all__'